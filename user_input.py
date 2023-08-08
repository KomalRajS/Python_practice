#basic
name = input("Enter your name : ")
age = int(input("Enter your age : "))

print(f"Hello {name}, you're {age} years old!!")
print()
print()

#mad lib
print("Let's play Mad Lib game")

noun=input("Enter a noun : ")
adj=input("Enter an adjective : ")
interjection=input("Enter an interjection : ")
verb = input("Enter a verb : ")

print(f"There is a {adj} house at the corner of the street")
print(f"{noun} {verb}s in that house")
print(f"{interjection}!! It was unbelievable!\n\n")

#area 
dia = float(input("Enter the diameter of the circle : "))
rad = dia/2
a1 = 3.14*rad*rad
print(f"The area of the circle is {round(a1,2)} cm^2")
print("\n")

#shopping cart
item = input("Enter the item you purchased : ")
price = float(input("Enter the price of 1 item in Rupees : "))
no = int(input(F"Enter the number of {item}s purchased : "))

total = price * no
print(f"Pay an amount of ₹{round(total,2)}")
print("Thank you!!!")