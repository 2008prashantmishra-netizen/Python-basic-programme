
'''name = input("Enter your name: ")
age = int(input("Enter your age: "))
age = age + 1

print(f" Hello {name}")
print(f" You are {age} years old")'''

# mad libs

'''adjective1 = input("Adjective: ")
noun = input("Noun: ")
adjective2 = input("Adjective: ")
verb = input("Verb: ")
adjective3 = input("Adjective: ")



print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun}")
print(f"{noun} was {adjective2} and {verb}ing.")
print(f"I was {adjective3}")'''

# area of rectangle

'''length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))
height = float(input("Enter the height of rectangle: "))

volume = length * width * height

print(f"the area is : {volume}cm^2")'''

# shopping cart

item = input("What item would you like to buy?: ")
price = float(input("What is the price of item?: "))
quantity = int(input("How many would you like? "))

total = price * quantity

print(f" You have bought {quantity}X {item}/s")
print(f"Your total is: ${round(total, 2)}")