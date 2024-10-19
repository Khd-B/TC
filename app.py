import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Temperature conversion functions
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
st.set_page_config(page_title="Interactive Temperature Converter", page_icon="🌡️")

# Set background color using CSS
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #f0f8ff;
    }
    .stButton>button {
        background-color: #4CAF50; /* Green */
        color: white;
    }
    .stButton>button:hover {
        background-color: #45a049; /* Darker green */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Interactive Temperature Converter")

value = st.number_input("Enter the temperature value:", value=0.0)
from_unit = st.selectbox("Select the unit of the temperature:", ['C', 'F', 'K'])
to_unit = st.selectbox("Select the unit to convert to:", ['C', 'F', 'K'])

if st.button("Convert"):
    with st.spinner("Converting..."):
        result = convert_temperature(value, from_unit, to_unit)
        
        if result is not None:
            st.success(f"{value}°{from_unit} is {result:.2f}°{to_unit}")
            
            # Plotting the temperature conversion
            x = np.arange(-100, 100, 1)
            if from_unit == 'C':
                y = celsius_to_fahrenheit(x)
                st.subheader("Celsius to Fahrenheit Conversion")
            elif from_unit == 'F':
                y = fahrenheit_to_celsius(x)
                st.subheader("Fahrenheit to Celsius Conversion")
            else:  # K
                y = kelvin_to_celsius(x + 273.15)
                st.subheader("Kelvin to Celsius Conversion")
            
            plt.figure(figsize=(10, 5))
            plt.plot(x, y, label=f"{from_unit} to {to_unit}", color='blue')
            plt.axhline(y=result, color='red', linestyle='--', label=f"Converted Value: {result:.2f}°{to_unit}")
            plt.title("Temperature Conversion Graph")
            plt.xlabel(f"Temperature in {from_unit}°")
            plt.ylabel(f"Temperature in {to_unit}°")
            plt.legend()
            plt.grid()
            st.pyplot(plt)

        else:
            st.error("Invalid units. Please use C, F, or K.")

# Add a footer with additional information
st.markdown("---")
st.markdown("Created with ❤️ by [Your Name](https://yourwebsite.com)")
