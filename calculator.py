print("================================")
print("       RVGA SMART CALCULATOR")
print("================================")
print("Developed by Ralph Vincent G. Atienza")
print("ITNT415 - BIT41")


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


while True:
    print("\n========== MENU ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("==========================")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Thank you for using Calculator Master.")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid menu choice. Please select 1-5.")
        continue

    try:
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", addition(first, second))

        elif choice == "2":
            print("Result:", subtraction(first, second))

        elif choice == "3":
            print("Result:", multiplication(first, second))

        elif choice == "4":
            if second == 0:
                print("Error: Cannot divide by zero.")
            else:
                print("Result:", division(first, second))

    except ValueError:
        print("Invalid input. Please enter numbers only.")
