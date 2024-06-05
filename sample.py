# print("Hello World")

# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# celsius = float(input("Enter temperature in Celsius: "))
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# celsius = float(input("Enter temperature in Celsius: "))

# fahrenheit = celsius_to_fahrenheit(celsius)

# message = "The temperature in Fahrenheit is: " + str(fahrenheit) + "°F"
# print(message)

# fahrenheit = celsius_to_fahrenheit(celsius)

# message = "The temperature in Fahrenheit is: " + str(fahrenheit) + "°F"
# print(message)

# celsius = float(input("Enter a temperature in Celsius: "))

# fahrenheit = (celsius * 9/5) + 32

# message = f"{celsius} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit."

# print(message)

def celsius_to_fahrenheit(celsius):
  """Converts Celsius temperature to Fahrenheit and returns the result."""
  return (celsius * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = celsius_to_fahrenheit(celsius)

message = "The temperature in Fahrenheit is: " + str(fahrenheit) + "°F"

print(message)
