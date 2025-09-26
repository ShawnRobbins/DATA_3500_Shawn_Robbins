# HW 3 Write a Python program, which solves the problems from the book: 3.4, 3.9, 3.11, 3.12,3.14 (Chapter 3, page 112).

# 3.4 fill in the missing code
for i in range(2):
    for j in range(7):
        print('@', end="")
    print()

# 3.9 Separating the digits of an integer
# Given a integer between 7 - 10 digits, loop through and pick of the left most digit to display
'''
The easy cheater method. Why deal with numbers at all?
userStr = input("Please enter a digit that is 7 - 10 numbers long:")
for num in userStr:
    print(num)
'''
userStr = input("Please enter a digit that is 7 - 10 numbers long:")
userNum = int(userStr)
startDivision = 1000000000
while userNum > 0:
    left_digit = userNum // startDivision
    if left_digit != 0:
        print(left_digit)
    userNum %= startDivision
    #print("Left Digit:", left_digit, "Number:", userNum)
    startDivision //= 10


# 3.11 Miles per gallon tracker
gallonsUsed = 0.0
milesDriven = 0
gallonsTotal = 0
milesTotal = 0
print("\nMPG Tracker")
while gallonsUsed != -1:
    gallonsUsed = float(input("Enter the gallons used (-1 to end): "))
    if gallonsUsed == -1:
        continue
    milesDriven = int(input("Enter the miles driven: "))
    gallonsTotal += gallonsUsed
    milesTotal += milesDriven
    print("The miles/gall for this tank was", milesDriven/gallonsUsed)
print("The overall average miles/gallon was", milesTotal/gallonsTotal, "\n")

# Palindrome checker
print("Palindrome Checker")
palTest = int(input("Enter a 5 digit number: "))
first_digit = palTest // 10000
second_digit = (palTest // 1000) % 10
forth_digit = (palTest % 100) // 10
fifth_digit = palTest % 10
#print("1st:", first_digit, "2nd:", second_digit, "4th:", forth_digit, "5th", fifth_digit)
if first_digit == fifth_digit and second_digit == forth_digit:
    print("palindrome!!!!")
else:
    print("not palindrome!")

# 3.14 <- this book thinks it is funny
# Compute the value of pi following an infinite series

pi = 4
denom = 3
sign = -1
for i in range(5000):
    pi = pi + ((4/denom)*sign)
    print("Iteration:", i, " - pi =", pi)
    denom += 2
    sign *= -1


