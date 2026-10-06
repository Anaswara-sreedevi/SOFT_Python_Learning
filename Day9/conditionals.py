# 30 Days of Python Learning Challenge
# Day 9: Conditionals in Python


# 1. Simple if statement
age = 18

if age >= 18:
    print("You are an adult.")


# 2. if-else statement
number = 10

if number > 0:
    print("The number is positive.")
else:
    print("The number is not positive.")


# 3. if-elif-else statement
marks = 75

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")


# 4. Checking even or odd
number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 5. Checking the largest of two numbers
a = 25
b = 40

if a > b:
    print("A is larger.")
elif b > a:
    print("B is larger.")
else:
    print("Both numbers are equal.")


# 6. Nested if statement
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You can enter.")
    else:
        print("You need an ID.")
else:
    print("You are not old enough.")


# 7. Using logical operators
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter the event.")
else:
    print("You cannot enter the event.")


# 8. Using or
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It is the weekend.")
else:
    print("It is a weekday.")


# 9. Using not
is_raining = False

if not is_raining:
    print("You can go outside.")
else:
    print("Take an umbrella.")


# 10. Membership with a conditional
fruits = ["apple", "banana", "orange"]

if "apple" in fruits:
    print("Apple is available.")


# 11. Comparing strings
password = "python123"

if password == "python123":
    print("Correct password.")
else:
    print("Incorrect password.")


# 12. Conditional expression (ternary operator)
age = 20

result = "Adult" if age >= 18 else "Minor"
print("Result:", result)


# 13. Checking a number range
number = 50

if 1 <= number <= 100:
    print("The number is between 1 and 100.")
else:
    print("The number is outside the range.")


# 14. Multiple conditions
temperature = 30

if temperature >= 35:
    print("Very hot")
elif temperature >= 25:
    print("Warm")
elif temperature >= 15:
    print("Cool")
else:
    print("Cold")


print("Day 9 completed: Learning Conditionals!")