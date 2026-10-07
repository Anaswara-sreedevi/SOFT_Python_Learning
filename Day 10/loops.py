# 30 Days of Python Learning Challenge
# Day 10: Loops in Python


# 1. for loop
for i in range(5):
    print("Number:", i)


# 2. for loop with a range
for i in range(1, 6):
    print(i)


# 3. Looping through a list
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print("Fruit:", fruit)


# 4. Looping through a string
word = "Python"

for letter in word:
    print(letter)


# 5. range() with a step
for i in range(0, 11, 2):
    print("Even number:", i)


# 6. while loop
count = 1

while count <= 5:
    print("Count:", count)
    count += 1


# 7. while loop with a condition
number = 10

while number > 0:
    print(number)
    number -= 1


# 8. break statement
for i in range(1, 11):
    if i == 6:
        break
    print("Number:", i)


# 9. continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print("Number:", i)


# 10. pass statement
for i in range(3):
    pass

print("Pass statement completed.")


# 11. Nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# 12. Multiplication table
number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# 13. Sum of numbers using a loop
total = 0

for i in range(1, 6):
    total += i

print("Sum:", total)


# 14. Finding even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for number in numbers:
    if number % 2 == 0:
        print("Even:", number)


# 15. Loop with else
for i in range(1, 6):
    print(i)
else:
    print("Loop completed.")


print("Day 10 completed: Learning Loops!")