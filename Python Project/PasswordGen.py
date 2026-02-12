import random
import string

length = int(input("How long is your password? "))

def generate_password(length=length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Generated Password:", generate_password())
