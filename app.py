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

def main():
    print("Temperature Converter")
    value = float(input("Enter the temperature value: "))
    from_unit = input("Enter the unit of the temperature (C, F, K): ").upper()
    to_unit = input("Enter the unit to convert to (C, F, K): ").upper()

    result = convert_temperature(value, from_unit, to_unit)
    
    if result is not None:
        print(f"{value}°{from_unit} is {result:.2f}°{to_unit}")
    else:
        print("Invalid units. Please use C, F, or K.")

if __name__ == "__main__":
    main()
