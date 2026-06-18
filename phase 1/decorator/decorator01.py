
def decorator_function(original_function):

    def wrapper_function():
        print("Wrapper function ran")
        return original_function()
    
    print("In Decorator function.")
    return wrapper_function

def display():
    print("Display function ran") 

decorated_display = decorator_function(display)

decorated_display()