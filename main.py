# temp_converter/main.py

from converter import celsius_to_fahrenheit, fahrenheit_to_celsius

def main():
    print("Welcome to the Temperature Converter!")
    choice = input("Choose conversion type:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nEnter 1 or 2: ")

    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C = {f}°F")
    elif choice == '2':
        f = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        print(f"{f}°F = {c}°C")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

