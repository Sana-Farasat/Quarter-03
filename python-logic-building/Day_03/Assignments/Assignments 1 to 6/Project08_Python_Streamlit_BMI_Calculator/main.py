import streamlit as st

st.set_page_config(page_title="Bmi Calculator")

st.title("BMI Calculator 🧮")

st.write("Enter your height and weight to calculate your Bmi")

height = st.number_input("height (in meters)" , min_value=0.5 , max_value=3.0 , value=1.75)

weight = st.number_input("weight (in kilograms)" , min_value=10 , max_value=90 , value=70)

if st.button("Calculate Bmi "):
    if height > 0 and weight > 0:
            bmi = weight / (height ** 2)
            st.success(f"Your Bmi is {bmi:.2f}")

            if bmi < 18.5:
                  st.warning("You are underweight 🟨")
            elif bmi < 24.9:
                  st.success("You have a normal weight 🟩")
            elif bmi < 29.9:
                  st.warning("You are overweight 🟨")
            else:
                  st.error("You are obese 🟥")

# Sidebar content
st.sidebar.markdown("""
### BMI Kya Hai? 🧮
**BMI (Body Mass Index)** is a simple method used to estimate whether a person has a healthy body weight for a given height. It helps identify if someone is underweight, normal weight, overweight, or obese, which can indicate potential health risks.
                    
### Formula to calculate BMI:
                    bmi = weight / (height ** 2)

**For example**: 
                     if a person weighs 70 kg and is 1.75 meters tall:
                     BMI = 70 / (1.75)² = 22.86
""")
