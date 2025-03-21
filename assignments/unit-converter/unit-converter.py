import streamlit as st 
 
 # Set page config with default light theme (This allows switching between dark and light)
st.set_page_config(page_title="Unit Converter")

#-----------------------Functionalities---------------------------

#----------------------Distance Converter Func--------------------
def distance_converter(from_unit, to_unit, value):
     units = {
            "Meters": 1,
            "Kilometers": 1000,
            "Feet": 0.3048,
            "Miles": 1609.34
     }
     result = value * units[from_unit] / units[to_unit]
     return result

#----------------------Temperature Converter Func--------------------
def temperature_converter(from_unit, to_unit, value):
    if from_unit == "Celcius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celcius":
        result = (value - 32) * 9/5
    else:
        result = value
    return result

#----------------------Weight Converter Func--------------------
def weight_converter(from_unit, to_unit, value):
    units = {
            "Kilograms": 1,
            "Grams": 0.001,
            "Pounds": 0.453592,
            "Ounces": 0.0283495
     }
    result = value * units[from_unit] / units[to_unit]
    return result

#----------------------Pressure Converter Func--------------------
def pressure_converter(from_unit, to_unit, value):
    units = {
            "Pascals": 1,
            "Hectopascals": 100,
            "Kilopascals": 1000,
            "Bar": 100000
     }
    result = value * units[from_unit] / units[to_unit]
    return result

#-----------------------User Interface----------------------------
# Use markdown with custom CSS to style the title

st.markdown("""
    <style>
    .title {
        color:  #3366CC !important;
        font-size: 50px !important;
        font-weight: bold !important;
        # text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Display the title using the custom CSS class
st.markdown('<h1 class="title">Unit Converter🔄</h1>', unsafe_allow_html=True)
st.write("unit converter is a simple app for converting various units of measurement quickly and easily.")
#st.title("Unit Converter")

category= st.selectbox("Select category",["Distance", "Temperature", "Weight", "Pressure"])

if category == "Distance":
   from_unit =  st.selectbox("From", ["Meters", "Kilometers", "Feet", "Miles"])
   to_unit =  st.selectbox("To", ["Meters", "Kilometers", "Feet", "Miles"])
   value =  st.number_input("Enter value")

   if st.button("Convert"):
       result = distance_converter(from_unit, to_unit, value)
       st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Temperature":
   from_unit =  st.selectbox("From", ["Celcius", "Fahrenheit"])
   to_unit =  st.selectbox("To", ["Celcius", "Fahrenheit"])
   value =  st.number_input("Enter value")

   if st.button("Convert"):
       result = temperature_converter(from_unit, to_unit, value)
       st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Weight":
   from_unit =  st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces"])
   to_unit =  st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"])
   value =  st.number_input("Enter value")

   if st.button("Convert"):
       result = weight_converter(from_unit, to_unit, value)
       st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Pressure":
   from_unit =  st.selectbox("From", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
   to_unit =  st.selectbox("To", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
   value =  st.number_input("Enter value")

   if st.button("Convert"):
       result = pressure_converter(from_unit, to_unit, value)
       st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")