#decorator using classes

class decorator:

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        return self.original_function(*args, **kwargs)

@decorator
def display():
    print("Display function ran") 

@decorator
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")


display()
display_info("Joviyal", 21)