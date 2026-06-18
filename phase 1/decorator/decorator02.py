
def decorator_function(original_function):

    def wrapper_function(*args, **kwargs):
        print("Wrapper function ran")
        return original_function(*args, **kwargs)
    
    print("In Decorator function.")
    return wrapper_function

@decorator_function
def display():
    print("Display function ran") 

@decorator_function
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")


display()

display_info("Joviyal", 21)