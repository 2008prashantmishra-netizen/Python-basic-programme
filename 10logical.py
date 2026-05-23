# logical operators = used an conditional statements

#       and = checks two or more conditions if true
#       or = checks if at least one condition is true
#       not = true if conditions is False, and vice versa

#temp = 40

'''if temp <= 0 and temp >= 30:
    print("The temprature is good")
else:
    print("The temprature is bad")'''
    
temp = 20
sunny = False
    
if temp <= 0 or temp >= 30:
    print("The temprature is bad")
else:
    print("The temprature is good")
    
if not sunny:
    print("It is cloudy outside")
else:
    print("It is sunny outside")