print("Calculator Master")
print("Developed by Ralph Vincent G. Atienza")
print("ITNT415 - BIT31")


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b


try:
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    print("Addition:", addition(first, second))
    print("Subtraction:", subtraction(first, second))

except ValueError:
    print("Invalid input. Please enter numbers only.")