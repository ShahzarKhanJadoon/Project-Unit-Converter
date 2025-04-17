# Import the Streamlit library for creating web applications
import streamlit as st

# Function to convert between different units
def convert_units(value, unit_from, unit_to):
    # Dictionary containing conversion factors between different units
    # Each key is in the format "fromUnit_toUnit" and the value is the conversion factor
    conversions = {
        "meter_kilometer": 0.001, #1 meter = 0.001 kilometer
        "kilometer_meter": 1000, #1 kilometer = 1000 meters
        "gram_kilogram": 0.001, #1 gram = 0.001 kilogram
        "kilogram_gram": 1000, #1 kilogram = 1000 grams
        "milliliter_liter": 0.001, #1 milliliter = 0.001 liters
        "liter_milliliter": 1000, #1 liter = 1000 milliliters
    }

    # Create a key by combining the from and to units
    key = f"{unit_from}_{unit_to}"
    
    # Check if the conversion is supported
    if key in conversions:
        # Get the conversion factor and calculate the result
        conversion_factor = conversions[key]
        return value * conversion_factor
    else:
        # Return an error message if the conversion is not supported
        return f"Conversion from {unit_from} to {unit_to} not supported"
    

# Set the title of the web application
st.title("Unit Converter") 

st.write("This is a simple unit converter that allows you to convert between different units of measurement.")
st.write("by Shahzar Khan")

# Create input field for the value to convert
value = st.number_input("Enter the value to convert")

# Create dropdown menus for selecting units
unit_from = st.selectbox("Select the unit to convert from", ["meter", "kilometer", "gram", "kilogram", "milliliter", "liter"])
unit_to = st.selectbox("Select the unit to convert to", ["meter", "kilometer", "gram", "kilogram", "milliliter", "liter"])

# Create a convert button and display the result when clicked
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.success(f"The converted value is {result}")


                              