"""
Simple script to test the backend API
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_health():
    """Test the health check endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/api/health")
        print(f"Health Check: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
    except Exception as e:
        print(f"Health Check Failed: {e}")

def test_register():
    """Test user registration"""
    try:
        data = {
            "name": "Test User",
            "email": "test@example.com",
            "password": "testpassword"
        }
        response = requests.post(f"{BASE_URL}/api/register", json=data)
        print(f"Register: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
        if response.status_code == 201:
            return response.json().get('access_token')
        elif response.status_code == 400:
            # User might already exist, try logging in
            print("User may already exist, trying login...")
            return test_login()
        else:
            return None
    except Exception as e:
        print(f"Register Failed: {e}")
        return None

def test_login():
    """Test user login"""
    try:
        data = {
            "email": "test@example.com",
            "password": "testpassword"
        }
        response = requests.post(f"{BASE_URL}/api/login", json=data)
        print(f"Login: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
        return response.json().get('access_token')
    except Exception as e:
        print(f"Login Failed: {e}")
        return None

def test_get_lectures(token):
    """Test getting lectures"""
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{BASE_URL}/api/lectures", headers=headers)
        print(f"Get Lectures: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
    except Exception as e:
        print(f"Get Lectures Failed: {e}")

if __name__ == "__main__":
    print("Testing Backend API")
    print("=" * 30)
    
    # Test health check
    test_health()
    print()
    
    # Test registration
    token = test_register()
    print()
    
    # If registration failed, try login
    if not token:
        token = test_login()
        print()
    
    # Test getting lectures
    if token:
        test_get_lectures(token)
        print()