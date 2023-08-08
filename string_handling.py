name = input("Enter your name : ")

#result = len(name)
name = name.capitalize()
#result = name.find("o")
#result = name.rfind("a")
#name = name.upper()
#name = name.lower()
#result = name.isalpha()
#result = name.isdigit()
#result = name.count("a")
#name = name.replace(" ","_")

#print(name)  
#print(result)

if name.find(" ") == -1:
    print(f"Hello, {name}!")
else :
    print("Do not enter spaces")

help(str)