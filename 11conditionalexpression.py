# conditional expression = A one-line shortcut for if-else statement (ternary operator)
#                         print or assign one of Two values based on condition 
#                         X if condition else Y

num = 8
a = 6
b = 7
age = 25
temprature = 30
user_role = "admin"

#print("Positive" if num > 0 else "Negative")
#result = "EVEN" if num % 2 == 0 else "ODD"
#max_num = a if a > b else b
#min_num = a if a < b else b
#status = "Adult" if age >= 18 else "Child"
#weather = "Hot" if temprature > 20 else "cold"
acess_level = "FULL ACCESS" if user_role == "admin" else "Limit me rahe laude"

print(acess_level)