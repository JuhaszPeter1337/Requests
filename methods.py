import requests

# GET
url = "http://127.0.0.1:8888/get-user/512"

res = requests.get(url = url)

print("GET method:\n")
print(f"Response text:\n{res.text}")
print(f"Response code:\n{res.status_code}\n")

# POST
url = "http://127.0.0.1:8888/create-user/632"

data = {"name": "John Doe"}

res = requests.post(url = url, json = data)

print("POST method:\n")
print(f"Response text:\n{res.text}")
print(f"Response code:\n{res.status_code}\n")

# DELETE
url = "http://127.0.0.1:8888/user"

res = requests.delete(url = url)

print("DELETE method:\n")
print(f"Response code:\n{res.status_code}")
