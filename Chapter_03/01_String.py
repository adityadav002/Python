# String is a sequence of characters
# String is Immutable.

# ********************************* String Literals ********************************************
# a = "Aditya"
# b = 'Aditya'
# c = '''Aditya'''
# d = """Aditya"""
# print(a)
# print(b)
# print(c)
# print(d)

# print()

# ********************************* Indexing ******************************************** 
# Name = "ADITYA"
# 0, 1, 2, 3, 4, 5  (front : 0 , length - 1)
# print(Name[0]) 
# print(Name[1])
# print(Name[2])
# print(Name[3])
# print(Name[4])
# print(Name[5])

# print()

# -6, -5, -4, -3, -2, -1  (back : length - 1, 0)
# print(Name[-6])
# print(Name[-5])
# print(Name[-4])
# print(Name[-3])
# print(Name[-2])
# print(Name[-1])

# print()

# ********************************* Slicing ******************************************** 
# name = "Aditya"
# print(name[0:3])  # start 0, end 3
# print(name[0:])  # start 0, end length - 1
# print(name[:4])  # start 0, end 3
# print(name[:])  # start 0, end length - 1

# a = "abcdefghi"
# print(a[0 : 4 : 2])  # start 0, end 4, step 2
# print(a[2 : 4 : 2])  # start 2, end 4, step 2

# print()

# ********************************* String Methods ******************************************** 
# name = "Aditya"
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.capitalize())
# print(name.swapcase())
# print(name.strip())
# print(len(name))
# print(name.count("a"))
# print(name.find("a"))
# print(name.endswith("tya"))
# print(name.startswith("Ad"))

# name = "Hello World"
# print(name.replace("World", "Aditya"))

# print()

# ********************************* String Formatting ******************************************** 
# name = "Aditya"
# age = 20
# print("My name is " + name + " and I am " + str(age) + " years old.")
# print("My name is {} and I am {} years old.".format(name, age))
# print(f"My name is {name} and I am {age} years old.")

# print()

# ********************************* String Concatenation ******************************************** 
# a = "Hello"
# b = "Aditya"
# c = a + " " + b
# print(c)

# print()

# ********************************* Escape Sequences ******************************************** 
# a = "Aditya Yadav \ncan \n\"code\" python"
# print(a)