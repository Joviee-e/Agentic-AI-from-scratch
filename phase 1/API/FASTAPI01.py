from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message" : "Welcome John"
    }

@app.get("/about")
def home():
    return {
        "name":"Joviee",
        "role":"Student"
        }