# import requests
# import time

# def call_api():
#     for retry in [1, 2, 4, 8]:  # Exponential backoff
#         response = requests.get("https://api.github.com/rate_limit")
#         if response.status_code == 429:  
#             time.sleep(retry)  # Retry after waiting
#         else:
#             print("YES")
#             return response.json()  


import requests

url = "https://api.github.com/rate_limit"
response = requests.get(url)

# Print Rate Limit Headers
print("X-RateLimit-Limit:", response.headers.get("X-RateLimit-Limit"))  # Total allowed requests
print("X-RateLimit-Remaining:", response.headers.get("X-RateLimit-Remaining"))  # Remaining requests
print("X-RateLimit-Reset:", response.headers.get("X-RateLimit-Reset"))  # Time when limit resets
