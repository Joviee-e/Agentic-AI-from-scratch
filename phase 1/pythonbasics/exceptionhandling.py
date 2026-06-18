
try:
    number = int(input("Enter a number:"))
    print(f"The number you entered is {number}")

except ValueError:
    print("Enter a valid number")

except:
    print("Something went wrong")