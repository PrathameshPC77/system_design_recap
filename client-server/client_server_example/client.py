import requests

# URL of the Django API endpoint
url = "http://127.0.0.1:8000/api/user/"

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("✅ Data received from server:")
        print(response.json())
    else:
        print(f"❌ Failed to fetch data. Status code: {response.status_code}")
except Exception as e:
    print(f"⚠️ Error while connecting to server: {e}")
