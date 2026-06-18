from fastapi import FastAPI

app = FastAPI()

@app.post("/add")
def add_student(student:dict):
    return {
        "received" : student
    }
