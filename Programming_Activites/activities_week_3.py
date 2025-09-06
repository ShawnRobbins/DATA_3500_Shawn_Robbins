# Programming Activity 1
apple_price = 1.5
number_purchased = 4
tax = 1.07

# calculate total price and print results
total_bill =  apple_price * number_purchased * tax
if total_bill == 0:
    print("Total bill is zero, please check inputs.")
print("You bought", number_purchased, "apples for", apple_price, "per apple.")
print("Total bill:", total_bill, "\n")

# Programming Activity 2
age = int(input("How old are you? "))
goalAge = int(input("What age would you like to live to? "))
yearsLeft = goalAge - age
print("You have approximately", yearsLeft,
    "left to live to accomplish your goals!\n")

# Programming Activity 3
userScore = int(input("What is your score as a percentage? (ex: 90)  "))
if userScore >= 93:
    print("Congratulations you got an A")
if userScore < 93:
    print("Congratulations, you still learned a ton!!!!")

# Additional Challenge One
"""First it prints: x = 2
Then it prints: Value of 2 + 2 is 4
Then it prints: x =
Finally prints: 5 x = 5"""

# Additional Challenge Two
print("Please enter 3 numbers, entering after each:")
num1 = eval(input("Number 1: "))
num2 = eval(input("Number 2: "))
num3 = eval(input("Number 3: "))

minNum = min(num1, num2, num3)
maxNum = max(num1, num2, num3)
print("The largest number is", maxNum, "\n"
    "The smallest number is", minNum)
if maxNum % 2 == 0:
    print("The range between the smallest and largest numbers is", minNum, "to", maxNum)
if maxNum % 2 != 0:
    if minNum <= 10 and minNum >= 0:
        print("The smallest number", minNum, "is within range of 0 to 10")
    if minNum < 0 or minNum > 10:
        print("The smallest number", minNum, "is not within range of 0 to 10")

