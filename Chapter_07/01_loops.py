# Loop through a list using a for loop
items = ["a1", "a2", "a3", "a4", "a5"]
for item in items:
    print(item)

print()

# Print "hello" with numbers 0 to 4
for i in range(5):
    print("hello", i)

print()

# Print numbers from 0 to 40 in steps of 4
for i in range(0, 41, 4):
    print(i)

print()

# Iterate over characters in a string
name = "ADITYADAV"
for char in name:
    print(char)

print()

# Iterate through a list of numbers
numbers = [12, 24, 36, 48]
for number in numbers:
    print(number)
else:
    print("done")

print()

# Break when i equals 5
for i in range(10):
    if i == 5:
        break
    print(i)

print()

# Skip iteration when i equals 5
for i in range(10):
    if i == 5:
        continue
    print(i)
