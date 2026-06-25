import random
import string

length = int(input("Enter password length: "))

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_characters = letters + digits + symbols

password = ''.join(random.choice(all_characters)
                   for _ in range(length))

print("\nGenerated Password:", password)