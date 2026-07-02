
#  PASSWORD GENERATOR

import random
import string

# Function to generate password
def generate_password(length, use_upper, use_lower, use_digits, use_symbols):

    characters = ""

    if use_upper:
        characters += string.ascii_uppercase

    if use_lower:
        characters += string.ascii_lowercase

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if characters == "":
        return "Please select at least one character type."

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


# Password Strength Function
def password_strength(length):

    if length <= 6:
        return "Weak Password"

    elif length <= 10:
        return "Medium Password"

    else:
        return "Strong Password"


# Main Program
print("=" * 55)
print("        WELCOME TO PASSWORD GENERATOR")
print("=" * 55)

while True:

    try:

        length = int(input("\nEnter Password Length: "))

        if length <= 0:
            print("Password length must be greater than 0.")
            continue

        print("\nSelect Characters to Include")

        upper = input("Include Uppercase Letters (Y/N): ").lower() == "y"
        lower = input("Include Lowercase Letters (Y/N): ").lower() == "y"
        digits = input("Include Numbers (Y/N): ").lower() == "y"
        symbols = input("Include Special Characters (Y/N): ").lower() == "y"

        password = generate_password(length, upper, lower, digits, symbols)

        print("\n" + "=" * 40)
        print("Generated Password")
        print("=" * 40)
        print(password)
        print("=" * 40)

        print("Password Strength :", password_strength(length))

        again = input("\nGenerate another password? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using Password Generator!")
            break

    except ValueError:
        print("\nInvalid Input! Please enter a valid number.")