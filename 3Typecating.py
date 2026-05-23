# typecasting = The process of converting a value of a data type to another data type.
#               (int, float, str, bool)
#               Explicit vs Implicit

"""name = "Prashant"
age = 21
gpa = 3.5   
student = True

'''print(type(name))
print(type(age))        
print(type(gpa))
print(type(student))'''

gpa = int(gpa) # explicit typecasting
print(type(gpa))

student = str(student) # explicit typecasting
print(type(student))

age = bool(age) # explicit typecasting
print(type(age))"""

# implicit typecasting

x=2
y=2.0

x = x / y
print(x)


