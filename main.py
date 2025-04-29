import requests

def make_request(url, *args, **kwargs):
    print("Extra args:", args)
    print("Request parameters:", kwargs)
    
    response = requests.get(url, params=kwargs)  # kwargs used for query parameters
    return response.json()

# Calling function with args & kwargs
make_request("https://api.example.com/data", "unused_arg", key="value", limit=5)