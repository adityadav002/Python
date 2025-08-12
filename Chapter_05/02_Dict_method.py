marks = {
    "Aditya": 100,
    "Yadav": 90,
    "Adi": 80,
    "list": [1, 2, 3]
}

# Dictionary Methods
print("Items:", marks.items())
print("Keys:", marks.keys())
print("Values:", marks.values())

# Update existing and add new key-value pairs
marks.update({"Aditya": 99, "Daddy": 95})
print("Updated Marks:", marks)

# Accessing values
print("Aditya's Marks (get):", marks.get("Aditya"))
print("Aditya's Marks (direct):", marks["Aditya"])

# Safe access with get (returns None if key doesn't exist)
print("Non-existing key (get):", marks.get("Adit"))
# print(marks["Adit"])  # Would raise KeyError

# Copying dictionary
new_dict = marks.copy()
print("Copied Dictionary:", new_dict)

# Creating new dictionary from keys with default value
keys = ['a', 'b', 'c', 'd']
new_dict = dict.fromkeys(keys, 0)
print("FromKeys Dictionary:", new_dict)

# Removing a key
removed_value = marks.pop("Adi")
print("Removed 'Adi':", removed_value)
print("After Pop:", marks)


# Items: dict_items([('Aditya', 100), ('Yadav', 90), ('Adi', 80), ('list', [1, 2, 3])])
# Keys: dict_keys(['Aditya', 'Yadav', 'Adi', 'list'])
# Values: dict_values([100, 90, 80, [1, 2, 3]])
# Updated Marks: {'Aditya': 99, 'Yadav': 90, 'Adi': 80, 'list': [1, 2, 3], 'Daddy': 95}
# Aditya's Marks (get): 99
# Aditya's Marks (direct): 99
# Non-existing key (get): None
# Copied Dictionary: {'Aditya': 99, 'Yadav': 90, 'Adi': 80, 'list': [1, 2, 3], 'Daddy': 95}
# FromKeys Dictionary: {'a': 0, 'b': 0, 'c': 0, 'd': 0}
# Removed 'Adi': 80
# After Pop: {'Aditya': 99, 'Yadav': 90, 'list': [1, 2, 3], 'Daddy': 95}