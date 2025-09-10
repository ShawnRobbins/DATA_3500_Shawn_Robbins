# Assignment Description: Write a Python program, which solves the problems from the book: 2.3, 2.4, 2.5, 2.6, 2.7, 2.8 (Chapter 2, page 71). 

# 2.3 
# Printing a message if the grade is over 89
grade = 92
if grade >= 90:
    print("Congratulations! Your grade of", grade, "earns you an A in the course\n")

# 2.4 
# 27.5 and 2 arithmetic
print(27.5+2)
print(27.5-2)
print(27.5*2)
print(27.5/2)
print(27.5//2)
print(27.5**2, "\n")

# 2.5
# Circle area, diameter, and circumference
pi = 3.14159
radius = 2
print("Info for a circle of radius", radius)
print("Diameter:", 2*radius)
print("Circumference:", 2*pi*radius)
print("Area:", pi*radius**2, "\n")

# 2.6 Odd or Even
number = eval(input("Give me a number: "))
if number % 2 == 0:
    print("Your number is even.")
else: 
    print("Your number is odd.")

# 2.7 Multiples
if 1024 % 4 == 0:
    print("1024 is a mutiple of 4.")
else:
    print("1024 is not a multiple of 4")
if 2 % 10 == 0:
    print("2 is a mutiple of 10.")
else:
    print("2 is not multiple of 10")

# 2.8 Table os square and cubes
print() #adding a space
print("number\tsquare\tcube")
for i in range(0, 6):
    print(i, i**2, i**3, sep="\t")