import random
import string
length = int(input("password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Your Password:", password)
