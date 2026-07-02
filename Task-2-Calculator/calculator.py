
# Task 2 - Simple Calculator
2
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


print("=" * 50)
print("        SIMPLE CALCULATOR")
print("=" * 50)

while True:

    try:
        # User Input
        num1 = float(input("\nEnter First Number : "))
        num2 = float(input("Enter Second Number : "))

        # Menu
        print("\nChoose an Operation")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("\nEnter Your Choice (1-5): ")

        # Perform Operation
        if choice == "1":
            print("\nResult =", add(num1, num2))

        elif choice == "2":
            print("\nResult =", subtract(num1, num2))

        elif choice == "3":
            print("\nResult =", multiply(num1, num2))

        elif choice == "4":
            print("\nResult =", divide(num1, num2))

        elif choice == "5":
            print("\nThank you for using the Calculator!")
            break

        else:
            print("\nInvalid Choice! Please select a valid option.")

        # Continue or Exit
        again = input("\nDo you want to perform another calculation? (yes/no): ").lower()

        if again != "yes":
            print("\nCalculator Closed Successfully.")
            break

    except ValueError:
        print("\nInvalid Input! Please enter numeric values only.")