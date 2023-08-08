name = "Raman"
age = 32
professor = True
years_of_exp = "5"
salary = 56.5
head_of_dept =""

print(type(name))
print(type(age))
print(type(years_of_exp))
print(type(professor))
print(type(salary))

#print(name+" is "+age+" years old")   cannot concatenate int to str
print(name+" is "+str(age)+" years old")
print(name,"is",age,"years old")
print(f"{name} is {age} years old")
print(f"Is raman a professor: {professor}")
print(f"Is {name}, the Head of the Department: {bool(head_of_dept)}")
print(f"{name}, who has {years_of_exp} years of experience, receives a salary of {salary}k Rupees per month")


#an example of casting
x,y,z = 12,36,99          #multiple variable assignment in case of same data type
#invalid - a,b = 6.4.3  
a = 4.8
print(f"data type of x is {type(x)}")
x = x/a                   #implicit casting
print(f"x = {x} and its datatype = {type(x)}")

#explicit type-casting
x=int(x)
print(f"Now, data type of x is {type(x)}")
y = bool(y)
print(f"y = {y} and its data type is {type(y)}")
z = float(z)
print(f"z = {z}")
a = str(a)
print(f"a = {a} and its data type is {type(a)}")
