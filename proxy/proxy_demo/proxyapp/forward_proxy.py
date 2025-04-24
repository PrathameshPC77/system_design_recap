import requests

def forward_request(url):
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # Proxy calling backend on your local Django server
    print(forward_request("http://127.0.0.1:8000/api/hello/"))
