import streamlit as st  # For UI
import sqlite3  # Built-in lightweight database
import hashlib  # For hashing passkeys
import os  # To manage file paths
from cryptography.fernet import Fernet  # For encryption/decryption


# Encrypt means hmari lkhi hue cheez koe prh na sake usy ksi formulae se change krdena k koe usy read na kr ske...
# Decrypt means hmari lkhi hue cheez ko uski actual form m wapis lana...

# Constants
KEY_FILE = "simple_secret.key"

# Load or generate encryption key
def load_key():
    if not os.path.exists(KEY_FILE):
        KEY = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(KEY)
    else:
        with open(KEY_FILE, "rb") as f:
            KEY = f.read()
    return KEY

# Initialize Fernet cipher
cipher = Fernet(load_key())

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect("simple_data.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS VAULT(
            lable TEXT PRIMARY KEY,
            encrypted_text TEXT,
            passkey TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db() # As app started, Database will be auto connected

# Hashkey : sha256 is a version of hashlib which converts keys into unique key by adding its 64 characters

# Hash passkey using SHA-256
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# text is converted into binary , binary is converted into fernet (encrypted code)
# encrypted code is that text which is not human readible
# encode() converts text into binary because fernet only works with binary
# fernet works only with binary

# Encrypt secret
def encrypt(text):
    return cipher.encrypt(text.encode()).decode()

# Decrypt secret
def decrypt(text):
    return cipher.decrypt(text.encode()).decode()

# Streamlit UI

st.set_page_config(page_title="Encrypt_Decrypt App")
st.title("🔐 Secure Data Encryption and Decryption App")

menu = ["Store Secret", "Retrieve Secret"]
choice = st.sidebar.selectbox("Choose Option", menu)

if choice == "Store Secret":
    st.header("🔒 Store a New Secret")

    label = st.text_input("Label (Unique ID):")
    secret = st.text_input("Your Secret:")
    passkey = st.text_input("Passkey (to protect it):", type="password")

    if st.button("Encrypt and Save"):
        if label and secret and passkey:
            conn = sqlite3.connect("simple_data.db")
            c = conn.cursor()

            encrypted = encrypt(secret)
            hashed_key = hash_passkey(passkey)

            try:
                c.execute("INSERT INTO VAULT (lable, encrypted_text, passkey) VALUES (?, ?, ?)",
                          (label, encrypted, hashed_key))
                conn.commit()
                st.success("✅ Secret saved successfully!")
            except sqlite3.IntegrityError:
                st.error("❗ Label already exists. Try another one.")
            conn.close()
        else:
            st.warning("⚠️ Please fill in all fields.")

elif choice == "Retrieve Secret":
    st.header("🔓 Retrieve Your Secret")

    label = st.text_input("Enter Label:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Decrypt"):
        conn = sqlite3.connect("simple_data.db")
        c = conn.cursor()
        c.execute("SELECT encrypted_text, passkey FROM VAULT WHERE lable=?", (label,))
        result = c.fetchone()
        conn.close()

        if result:
            encrypted, hashed_key = result
            if hash_passkey(passkey) == hashed_key:
                decrypted = decrypt(encrypted)
                st.success("✅ Here is your secret:")
                st.code(decrypted)
            else:
                st.error("❌ Incorrect passkey!")
        else:
            st.warning("⚠️ No such label found.")
