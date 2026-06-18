import requests

print("Before sending data")
response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"
)
print(response.json())

data = {
    "name" : "Joviee",
    "age" : 21
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/users", 
    json=data
)
print("\nPosting a data:\n")
print(response.json())