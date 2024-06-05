def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    friendly_message = "The temperature " + str(celsius) + "°C is equal to " + str(fahrenheit) + "°F."
    print(friendly_message)

if __name__ == "__main__":
    main()
