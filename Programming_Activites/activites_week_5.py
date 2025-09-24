"""
Programming Activity 1

Write a program which can tell if a 3 digit number is a palindrome. 
 - Create a variable, which stores user input. Prompt the user to enter a 3 digit number. 
 - Convert the user input into a integer (int). To get the first digit alone, floor division by 100. 
 - To get the 3rd digit alone, modulus by 10. 
 - Check if the first digit and 3rd digit are the same. 
 - If they are the same print("palindrome!!!!"). 
 - Else print("not palindrome!")
"""
print("Palindrome number checker:")
num = int(input("Please enter a 3 digit number: "))
first_digit = num // 100
third_digit = num % 10
if first_digit == third_digit:
    print("palindrome!!!!")
else:
    print("not palindrome!")


"""
Programming Activity 2

Write a program which can adds up the numbers in the series:
1/2 + 1/4 + 1/8 + 1/16 + 1/32 for 1000 iterations.
create a variable for the denominator
for loop for 1000 iterations
start for loop at 1, go to 1000
variable to track the sum
What number is the result?
"""
denominator = 2
loop_sum = 0.0
for num in range(1, 1001):
    loop_sum += 1 / denominator
    denominator *= 2
    # if num % 25 == 0:
    #     print("Iteration", num, "Sum:", loop_sum)
print("Final Sum:", loop_sum)
#The result is real close to 1, but it just rounds there after 75 iterations

"""
Programming Activity 3

Write a program which determines whether a child can sit in the front seat  of a car, using the following logic:
- if a child is 12 years old or older, they can sit in the front, regardless of weight.
- if a child is 11 years old, and over 90 pounds, they can sit in the front seat.
- if a child is under 11 years old, and over 100 pounds, they can sit in the front seat
- if a child does meet the criteria above they cannot sit in the front seat.
Your program will ask the user for a child's age and weight. Use Boolean variables to store the results of the criteria above. 
Use if statements and the Boolean variables created above to print a message to the user whether or not the child may sit in the front seat.
"""
age = int(input("How old is your child? "))
weight = int(input("How much does your child weigh (in lbs)? "))

age_12 = age >= 12
age_11 = age >= 11 and weight > 90
hefty = age < 11 and weight > 100

if age_12 or age_11 or hefty:
    print("Your child can sit in the front seat.")
else:
    print ("Your child cannot sit in the front seat")

"""
Programming Activity 4

Write a function named "welcome_fctn" which takes one argument, called "name".  Inside the function, print to the console "Welcome " name.
- Use the def command to define a function "welcome_fctn"
- Add a parameter list with one variable "name", i.e. (name)
- Print "Welcome " name in the function body.
- We don't need a return statement here, but keep in mind python does return nothing.
- Call the function, welcome_fctn(<your_name>)
"""
def welcome_fctn(name, age, favorite_color):
    welcome_message = "Welcome " + name + ", you are " + str(age) + " years old, and " + favorite_color + " is your favorite color."
    return(welcome_message)

print(welcome_fctn("Shawn", 31, "orange"))

"""
Programming Activity 5

Update the function in activity one, and create a new string variable in the function called, welcome_message. The variable welcome_message should be 
assigned the value "Welcome " name. The same value printed in activity 1, but here you save it as a variable. Return the variable welcome_message.
- Assuming your function in programming activity 1 works, you will need to:
- Create a variable to store "Welcome " + name
- Return the value welcome_message
- There are a couple ways to test this. you could
         1. Print(welcome_fctn("Bob"))
         2. Create a variable to store what is returned by the function then print that
"""

"""
Programming Activity 6

Update the function in activity one to have 3 variables: name (string),  age (int), favorite_color (string).  Create a new variable called welcome_message and 
assign it to the value "Welcome <name>, you are <age> years old, and <favorite_color> is your favorite color".  Return the variable welcome_message.
- Add two variables to your parameter list
- Concatenate those two variables in your welcome_message
- Return welcome_message just like you did in activity 2
- To test this, call welcome_fctn with 3 arguments
"""


"""
1. Write a Python program that simulates a simple ATM machine. The program should ask the user for their account balance and then offer them the following 
options in a loop:

Check Balance
Deposit Money
Withdraw Money
Quit
If the user selects "Check Balance," display their current balance. If they select "Deposit Money," ask how much they want to deposit and update the balance 
accordingly. If they select "Withdraw Money," ask how much they want to withdraw and update the balance if they have sufficient funds. If they select "Quit," 
exit the program. Make sure to use nested if statements for handling these options.
"""

"""
2. Write a Python program to generate a multiplication table for a given number. Ask the user to enter a number, and then use the range() function to generate a table of multiplication from 1 to 10 for that number. For example, if the user enters 5, the program should print:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
"""

"""
3. Write a Python program that checks the strength of a user's password. Password strength is determined by the following rules:

The password must be at least 8 characters long.
The password must contain at least one uppercase letter.
The password must contain at least one lowercase letter.
The password must contain at least one digit.
The password may contain special characters (e.g., !, @, #, $, etc.), but it is not required.
Your program should prompt the user to enter a password, and then it should determine whether the password meets these criteria.

Example Input/Output:
# Input
password = "SecureP@ssw0rd"
# Output
Password is strong!

# Input
password = "weak"
# Output
Password is weak. It does not meet the criteria.
"""

"""
4. You are building a weather decision-making system for a camping trip. To decide whether to go camping, you need to consider the weather conditions and other factors. You will make the decision based on the following criteria:

The weather should be either clear or partly cloudy.
The temperature should be between 50°F (10°C) and 85°F (30°C).
It should not be raining or snowing.
It should not be too windy (wind speed less than 20 mph).
Your program should prompt the user to enter the current weather conditions, temperature, and wind speed, and then determine whether it's a good day to go camping.

Write a Python program for weather-based decision-making that takes weather conditions, temperature, and wind speed as input and checks if it's a good day for camping based on the criteria above. Display a message indicating whether it's a good day to go camping or not.
"""