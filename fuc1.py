import requests

request = f"http://api.chucknorris.io/jokes/random"

jokes = requests.get(request).json()

print(jokes["value"])