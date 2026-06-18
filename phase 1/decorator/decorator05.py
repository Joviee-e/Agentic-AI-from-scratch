
def decorator(func):
    def wrapper(password):
        if password == "admin123":
            return func()
        else:
            print("Incorrect password. Access denied.")

    return wrapper

@decorator
def check_password():
    print("Password is correct")
    print("welcome to admin panel")


password = str(input("Enter password: "))
check_password(password)


