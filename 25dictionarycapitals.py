# dictionary = a collection of {key: value} pairs
#            ordered and changeable. NO duplicates

capitals = {"USA": "Washington D.C.",
            "INDIA": "New Delhi",
            "CHINA": "Beijing",
            "RUSSIA": "Moscow"}

#print(dir(capitals))        
#print(help(capitals))
#print(capitals.get("USA"))

#if capitals.get("Japan"):
 #   print("That capital exist's")
#else:
 #   print("That capitals doesn't exist")
 
#capitals.update({"GERMANY": "Berlin"})
#capitals.update({"USA": "Detroit"})
#capitals.pop("CHINA")
#capitals.popitem()
#capitals.clear()

#keys = capitals.keys()
#for key in capitals.keys():
   # print(key)
   
#values = capitals.values()
#for value in capitals.values():
 #   print(value)
 
 
items = capitals.items()

for key, value in capitals.items():
    print(f"{key}: {value}")