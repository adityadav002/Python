marks = {
    "Aditya": 100,
    "Yadav": 90,
    "Adi": 80,
    "list": [1, 2, 3]
}

# Display the dictionary and its type
print("Marks Dictionary:", marks)
print("Type:", type(marks))

# Access and display the list value
print("List Value:", marks["Adi"])
print("List Value:", marks["list"])

print()
#how to add user info
data = input("Enter your data: ")
value = input("Enter your value: ")
marks[data] = value
print("Marks Dictionary:", marks)



