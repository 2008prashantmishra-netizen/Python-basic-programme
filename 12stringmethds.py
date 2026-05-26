
#name = input("Enter your full name: ")
#phone_number = input("Enter your phone #: ")

#result = len(name)
#result = name.find("")
#result = name.rfind("")
#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#result = name.isdigitI()
#result = name,isalpha()
#phone_number = phone_number.count("-", "")
#phone_number = phone_number.replace("-", "")

#print(phone_number)


#print(help(str))


# validate user input exercise
# 1. username is no no more than 12 characters 
# 2. username must not contains spaces 
# 3. username must not contain digits 

username = input(" Enter a username: ")

if len(username) > 12:
    print("Your username can not be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"WELCOME {username}")
