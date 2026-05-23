# weight converter

weight = float(input("Enter Your Weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is: {round(weight, 1)} {unit}")
    
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs"
    print(f"Your weight is: {round(weight, 1)} {unit}")
    
else:
    print(f"{unit} chodu sahi unit daal")


 
 # Weight Converter

# chat gpt

'''weight = float(input("Enter Your Weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is: {round(weight, 1)} {unit}")

elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is: {round(weight, 1)} {unit}")

else:
    print(f"{unit} is not a valid unit")'''