# # Programming activity 1 
# year = int(input("What year were you born? "))
# if year >= 2010:
#     print("You belong to the Gen Alpha Generation\n")
# elif year >= 1997:
#     print("You belong to the Zoomer Generation\n")
# elif year >= 1981:
#     print("You belong to the Millennial Generation\n")
# elif year >= 1965:
#     print("You belong to the Gen X Generation\n")
# elif year >= 1946:
#     print("You belong to the Baby Boomer Generation\n")
# else:
#     print ("You're real old.\n")

# # Programming Activity 2
# current_year = 2025
# age = int(input("How old are you? "))
# while age > 1:
#     print("You were alive in year:", current_year)
#     age -= 1
#     current_year -= 1
# else:
#     current_year -= 1
#     print("You were born in year:", current_year, '\n')

# # Programming activity 3
# for i in range(5, 96):
#     if i % 5 == 0:
#         print(i)

# # Programming activity 4
# j = 5
# while j < 96:
#     if j % 5 == 0:
#         print(j)
#     j += 1

# # Additional Challenge 1
# '''
# Generate a random number between 1 and 100
# Get user guess for number
# Let them know if it is too high, too low, or correct
# Continue until user guess correctly or quits
# Keep track of the number of guesses
# '''
# import random

# # Generate a random number between 1 and 100
# num_to_guess = random.randint(1, 100)
# user_guess = -1
# #Keep track of the number of guesses
# attempts = 0
# print("Guess a number between 1 and 100!")
# print("(enter 0 to quit)")
# #Continue until user guess correctly or quits
# while user_guess != num_to_guess and user_guess != 0:
#     # Get user guess for number
#     user_guess = int(input("Enter your guess: "))
#     #Let them know if it is too high, too low, or correct
#     attempts +=1
#     if user_guess == 0:
#         print("Goodbye.\n")
#     elif user_guess > num_to_guess:
#         print("Too high.")
#     elif user_guess < num_to_guess:
#         print("Too low.")
#     else:
#         print("Correct! It took you", attempts, "guesses.\n")

# # Additional Challenge 2. Find all the prime numbers within a given range using a for loop
import math
print("Prime Number Finder\nPlease enter a range:")
range_start = int(input("From: "))
range_end = int(input("To: "))

for num in range(range_start, range_end+1):
    is_prime = False
    if num >= 1:
        if num == 2:
            print(num)
        elif num % 2 != 0:
            for i in range(3, int(math.sqrt(num)) + 1, 2):
                if num % i != 0:
                    print(num)
                    



# Additional Challenge 2.5. Write a Python program to reverse a given three or more digit integer WITHOUT using lists (hint, use // and % to isolate numbers)
