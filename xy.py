def add(a,b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
def main():
    print("Welcome to the simple calculator!")
    print("You can perform addition, subtraction, multiplication, and division.")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(f"Addition: {add(a, b)}")
    print(f"Subtraction: {subtract(a, b)}")
    print(f"Multiplication: {multiply(a, b)}")
    print(f"Division: {divide(a, b)}")
if __name__ == "__main__":
    main()
