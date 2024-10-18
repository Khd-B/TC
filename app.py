import streamlit as st

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'C':
        if to_unit == 'F':
            return celsius_to_fahrenheit(value)
        elif to_unit == 'K':
            return celsius_to_kelvin(value)
    elif from_unit == 'F':
        if to_unit == 'C':
            return fahrenheit_to_celsius(value)
        elif to_unit == 'K':
            return fahrenheit_to_kelvin(value)
    elif from_unit == 'K':
        if to_unit == 'C':
            return kelvin_to_celsius(value)
        elif to_unit == 'F':
            return kelvin_to_fahrenheit(value)
    
    return None

# Streamlit UI
st.title("Temperature Converter")

value = st.number_input("Enter the temperature value:", value=0.0)
from_unit = st.selectbox("Select the unit of the temperature:", ['C', 'F', 'K'])
to_unit = st.selectbox("Select the unit to convert to:", ['C', 'F', 'K'])

if st.button("Convert"):
    result = convert_temperature(value, from_unit, to_unit)
    
    if result is not None:
        st.success(f"{value}°{from_unit} is {result:.2f}°{to_unit}")
    else:
        st.error("Invalid units. Please use C, F, or K.")
