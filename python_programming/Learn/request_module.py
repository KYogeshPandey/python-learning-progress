import requests

# GET request
response = requests.get("https://www.youtube.com/")
print(response.status_code)
print(response.text)

# POST request
url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=data, headers=headers)

print(response.status_code)
print(response.json())