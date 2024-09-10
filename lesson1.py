# ASSIGNMENT 1 - Wednesday, September 4th
# 1. Ask the user for their name and age, then greet them by name, and tell them how old they will be in 100 years.
#     Use f-strings, not concatenation.
# 2. Create a tip calculator program using functions and user input. Use a return statement in your function.

# Make sure your assignments are done by Tuesday at 11:59pm the day before our next session.
#     We will review your code the next morning before the session that evening.

# HAPPY CODING!

#Asking for age and name

name= input ("Please enter your name? ")
age= int(input ("Please enter your age? "))

age_in_100_years = age + 100


print(f"Hello, {name}! You will be {age_in_100_years} in 100 years ")

#Calculator program
