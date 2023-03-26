import requests

api_key = "<API KEY HERE>"

with open("api_key.txt") as f:
    data = requests.get(f"https://api.polygon.io/v1/open-close/AAPL/2023-03-24?adjusted=true&apiKey={api_key).json()

print(data["close"])
