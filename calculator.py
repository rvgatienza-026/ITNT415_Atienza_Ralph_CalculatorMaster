print("Calculator Master")
print("Developed by Ralph Vincent G. Atienza")
print("ITNT415 - BIT31")


def addition(a, b):
    return a + b


try:
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    result = addition(first, second)

    print(f"{first} + {second} = {result}")

except ValueError:
    print("Invalid input. Please enter numbers only.")