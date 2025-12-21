import requests
import json

# First, let's login to get a token
login_data = {
    "email": "test@example.com",
    "password": "testpassword"
}

response = requests.post("http://localhost:5000/api/login", json=login_data)
print("Login Response:")
print(f"Status Code: {response.status_code}")
print(json.dumps(response.json(), indent=2))

if response.status_code == 200:
    token = response.json().get('access_token')
    print(f"\nToken: {token}")
    
    # Now let's try to get lectures with the token
    headers = {"Authorization": f"Bearer {token}"}
    lectures_response = requests.get("http://localhost:5000/api/lectures", headers=headers)
    print("\nLectures Response:")
    print(f"Status Code: {lectures_response.status_code}")
    print(json.dumps(lectures_response.json(), indent=2))