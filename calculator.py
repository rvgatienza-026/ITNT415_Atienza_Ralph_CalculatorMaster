print("Calculator Master")
print("Developed by Ralph Vincent G. Atienza")
print("ITNT415 - BIT41")


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        print("Error: Cannot divide by zero.")
    else:
        print(f"{a} / {b} = {a / b}")


try:
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    print("Addition:", addition(first, second))
    print("Subtraction:", subtraction(first, second))
    print("Multiplication:", multiplication(first, second))
    print("Division:")
    division(first, second)

except ValueError:
    print("Invalid input. Please enter numbers only.")