import requests
import json

def send_post_request():
    url = "http://localhost:5000/users"
    with open('Users.json', 'r', encoding='utf-8') as f:
        users = json.load(f)
    for user in users:
        response = requests.post(url, data=json.dumps(user, ensure_ascii=False).encode('utf-8'), headers={'Content-Type': 'application/json; charset=utf-8'})
        if response.status_code == 201:
            print(f"POST request for {user['name']} was successful.")
        else:
            print(f"POST request for {user['name']} failed with status code: {response.status_code}")
