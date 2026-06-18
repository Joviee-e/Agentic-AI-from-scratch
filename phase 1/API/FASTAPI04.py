from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int

students = [
    Student(name="John", age=21),
    Student(name="Joviyal", age=21)
]


@app.post("/student")
def create_student(student: Student):
    students.append(student)
    return {
        "message": "Student added successfully"
    }

@app.get("/student-info")
def list_students():
    return students

@app.get("/search-student")
def search_student(name: str):

    if len(students) == 0:
        return {
            "message": "No students found"
        }

    for student in students:
        if student.name.lower() == name.lower():
            return {
                "message": "Student exists",
                "student": student
            }

    return {
        "message": "Student does not exist"
    }

@app.get("/count")
def student_count():
    return { 
        "total students" : len(students)
    }

@app.get("/student-above-age")
def above_age(age : int):
    if len(students) == 0:
        return { 
            "message" : "No students present in list pls add"
        }
    age_list = []
    for student in students:
        if student.age > age:
            age_list.append(student)

    return {
        "message" : "found students above mentioned age",
        "students" : age_list
    }

@app.put("/update-student")
def update_student(name: str,new_name:str, age: int):

    if len(students) == 0:
        return {
            "message": "No students found"
        }

    for student in students:

        if student.name.lower() == name.lower():
            student.name = new_name
            student.age = age

            return {
                "message": "Student updated successfully",
                "student": student
            }

    return {
        "message": "Student not found"
    }

@app.delete("/delete-student")
def delete_student(name: str):

    if len(students) == 0:
        return {
            "message": "No students found"
        }

    for student in students:
        if student.name.lower() == name.lower():
            students.remove(student)

            return {
                "message": "Student deleted successfully"
            }

    return {
        "message": "Student not found"
    }


@app.get("/students-between-age")
def students_between_age(min: int, max: int):

    result = []

    for student in students:

        if min <= student.age <= max:
            result.append(student)

    if len(result) == 0:
        return {
            "message": "No students found"
        }

    return {
        "students": result
    }