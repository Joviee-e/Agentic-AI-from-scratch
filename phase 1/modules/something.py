import modueee as module

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = module.addition(a, b)
    print(f"The result of addition is: {result}")

except ValueError:
    print("Please enter a valid number")