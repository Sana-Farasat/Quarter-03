import streamlit as st

# Page settings
st.set_page_config(page_title="Calculator")

# Title and description
st.header("Calculator ➕➖✖➗")
st.write("Simple calculator to calculate all operations.")

# Calculator function
def Calculator():

    # User input
    num1 : int = st.number_input("Enter your first number: ")
    num2 : int = st.number_input("Enter your second number: ")
    operator = st.selectbox( "Select an operator:", ("+", "-", "*", "//" , "**" , "%"))

     # When user clicks the button
    if st.button("Calculate"):
        if operator == "+":
            result = num1 + num2
            st.success(f"The sum of {num1} and {num2} is {result}.")
        elif operator == "-":
            result = num1 - num2
            st.success(f"The difference of {num1} and {num2} is {result}.")
        elif operator == "*":
            result = num1 * num2
            st.success(f"The multiplication of {num1} and {num2} is {result}.")
        elif operator == "//":
            if num2 != 0:
                result = num1 // num2
                st.success(f"The floor division of {num1} by {num2} is {result}.")
            else:
                st.error("Cannot divide by zero.")
        elif operator == "**":
            result = num1 ** num2
            st.success(f"{num1} raised to the power {num2} is {result}.")
        elif operator == "%":
            if num2 != 0:
                result = num1 % num2
                st.success(f"The modulus of {num1} and {num2} is {result}.")
            else:
                st.error("Cannot find modulus with zero.")
        else:
            st.error("Invalid input..")

# Sidebar
st.sidebar.markdown("## 📊 About This App")
st.sidebar.markdown("""
This is a **Simple Calculator App** built using **Streamlit**.

You can perform basic mathematical operations:

- ➕ Addition  
- ➖ Subtraction  
- ✖ Multiplication  
- ➗ Floor Division  
- 🔢 Modulus  
- 🧮 Exponentiation

---

👨‍💻 **Created by:** Sana Farasat  
📅 **Date:** 17 April 2025  
""")

# Call the function
Calculator()


            

    
