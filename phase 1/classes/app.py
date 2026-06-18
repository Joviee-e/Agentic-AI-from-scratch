from Student import Student

try:
    student1 = Student("Alice", 20, "Female")
    student2 = Student("Bob", 22, "Male")
except Exception as e:
    print(f"Error occurred: {e}")