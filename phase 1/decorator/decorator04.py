
def decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@decorator
def convert_to_uppercase():
    return "hello world"


print(convert_to_uppercase())