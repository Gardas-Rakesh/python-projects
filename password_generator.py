import random
import string
length = int(input("Enter password length: "))
characters = string.ascii_letters

choice = input("Include numbers? (y/n): ")
if choice == 'y':
    characters += string.digits

choice = input("Include symbols? (y/n): ")
if choice == 'y':
    characters += string.punctuation
password = ''.join(random.choice(characters) for i in range(length))
print("Generated Password:", password)