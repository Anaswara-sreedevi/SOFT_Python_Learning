# Day 8: Dictionaries

# 1. Creating a dictionary
student = {
    "name": "Anaswara",
    "age": 18,
    "course": "BCA"
}
print("Student:", student)


# 2. Accessing values
print("Name:", student["name"])
print("Course:", student["course"])


# 3. Using get()
print("Age:", student.get("age"))
print("College:", student.get("college", "Not available"))


# 4. Adding a new item
student["college"] = "Jain University"
print("After adding college:", student)


# 5. Updating a value
student["age"] = 19
print("After updating age:", student)


# 6. Removing an item
student.pop("age")
print("After removing age:", student)


# 7. Checking if a key exists
if "name" in student:
    print("Name exists in the dictionary")


# 8. Dictionary keys
print("Keys:", student.keys())


# 9. Dictionary values
print("Values:", student.values())


# 10. Dictionary items
print("Items:", student.items())


# 11. Looping through a dictionary
for key, value in student.items():
    print(key, ":", value)


# 12. Nested dictionary
students = {
    "student1": {
        "name": "Anaswara",
        "course": "BCA"
    },
    "student2": {
        "name": "Akhil",
        "course": "BCA"
    }
}

print("Nested dictionary:", students)
print("Student 1 name:", students["student1"]["name"])


# 13. Dictionary comprehension
squares = {x: x ** 2 for x in range(1, 6)}
print("Squares:", squares)