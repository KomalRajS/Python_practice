import math

# argumented assignment operators
i = 7
print(i)
i += 5
print(i)
i -= 3
print(i)
i **= 2           ##exponential
print(i)
print("\n")

#built-in functions
a = 7.5
print(f"a = {a}")
b = round(a)
print(f"round = {b}")
print(f"abs = {abs(a)}")
print(f"absolute value of -2 is {abs(-2)}")
print()

#math module
print(f"ceil = {math.ceil(a)}")
print(f"floor = {math.floor(a)}")
print(f"value of e = {math.e}")
print(f"square root = {math.sqrt(a)}")
print("\n")

#Exercise-1
r = float(input("Enter the radius of the circle : "))
area = math.pi * pow(r,2)
circumference = math.pi * 2 * r
print(f"Area of the circle = {round(area,2)}")
print(f"Circumference of the circle = {round(circumference,2)}\n")

#Exercise - 2
a = float(input("Enter adjacent side A of the triangle : "))
b = float(input("Enter opposite side B of the triangle : "))
c = math.sqrt(pow(a,2) + pow(b,2))
print(f"The hypotenuse side C of the triangle is : {round(c,2)}")