import random
import string

def generate_password(length, letters, numbers, symbols):
    characters = ''
    if letters:
        characters += string.ascii_letters  # add letters a-z, A-Z
    if numbers:
        characters += string.digits         # add 0-9 
    if symbols:
        characters += string.punctuation    # add symbols

    if not characters:
        return "No character types selected!"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print("|----------------------|")
print("|  PASSWORD GENERATOR  |")
print("|----------------------|")

length = int(input("Enter the length: "))

letters = input("Include letters? (y/n): ").lower() == 'y'
numbers = input("Include numbers? (y/n): ").lower() == 'y'
symbols = input("Include symbols? (y/n): ").lower() == 'y'

password = generate_password(length, letters, numbers, symbols)
print("\nGenerated Password: ", password)
