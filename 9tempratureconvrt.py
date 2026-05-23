# temprature converter

unit = input("In this temprature in Celcius or Farenheit (C\F): ")
temp = float(input("Enter the temprature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f" The temprature in Farenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f" The temprature in Celcius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit measurement")