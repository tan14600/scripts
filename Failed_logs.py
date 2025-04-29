import requests

def fetch_data_from_api():
    url = "https://api.github.com/users/tan14600"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for 4xx/5xx responses
        print(type(response))
        data = response.json()  # Parse JSON response
        # print(data)
        if(data["following"]<10):
            print("User:", data["login"])
            print("Public Repos:", data["public_repos"])
        else:
            print("Famous")
    except requests.exceptions.RequestException as e:
        print(f"API Request Failed: {e}")

fetch_data_from_api()


##rate limit

import requests
import time

url = "https://api.example.com/data"

for i in range(5):  # Retry up to 5 times
    response = requests.get(url)
    
    if response.status_code == 429:  # Too many requests
        retry_after = int(response.headers.get("Retry-After", 10))  # Default to 10s
        print(f"Rate limit exceeded. Retrying in {retry_after} seconds...")
        time.sleep(retry_after)
    else:
        print("Success:", response.json())
        break


## Invalid response
import requests

url = "https://api.example.com/data"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises HTTPError for bad responses
    data = response.json()
    
    if "expected_field" in data:
        print("Valid response:", data)
    else:
        print("Unexpected response format!")

except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Something went wrong:", err)


## Authemticate
import requests

headers = {"Authorization": "Bearer YOUR_API_KEY"}
response = requests.get("https://api.example.com/protected-data", headers=headers)
print(response.json())