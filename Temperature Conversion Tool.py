def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    while True:
        print("\nTemperature Conversion Tool")
        print("1. Celsius to Fahrenheit")
        print("2. Celsius to Kelvin")
        print("3. Fahrenheit to Celsius")
        print("4. Fahrenheit to Kelvin")
        print("5. Kelvin to Celsius")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")

        try:
            choice = int(input("Select an option: "))
            if choice == 1:
                celsius = float(input("Enter temperature in Celsius: "))
                print(f"{celsius} Celsius is {celsius_to_fahrenheit(celsius):.2f} Fahrenheit")
            elif choice == 2:
                celsius = float(input("Enter temperature in Celsius: "))
                print(f"{celsius} Celsius is {celsius_to_kelvin(celsius):.2f} Kelvin")
            elif choice == 3:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                print(f"{fahrenheit} Fahrenheit is {fahrenheit_to_celsius(fahrenheit):.2f} Celsius")
            elif choice == 4:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                print(f"{fahrenheit} Fahrenheit is {fahrenheit_to_kelvin(fahrenheit):.2f} Kelvin")
            elif choice == 5:
                kelvin = float(input("Enter temperature in Kelvin: "))
                print(f"{kelvin} Kelvin is {kelvin_to_celsius(kelvin):.2f} Celsius")
            elif choice == 6:
                kelvin = float(input("Enter temperature in Kelvin: "))
                print(f"{kelvin} Kelvin is {kelvin_to_fahrenheit(kelvin):.2f} Fahrenheit")
            elif choice == 7:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

main()