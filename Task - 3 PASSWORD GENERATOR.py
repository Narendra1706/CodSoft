# Task - 3 PASSWORD GENERATOR

import random
import string

while True:
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive integer for the length.")
            continue
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        continue

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated Password: {password}")

    choice = input("Do you want to generate another password? (yes/no): ").strip().lower()
    if choice != 'yes':
        print("Exiting the password generator. Goodbye!")
        break