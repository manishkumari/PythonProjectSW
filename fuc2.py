import requests
import json
api_key = "6d2e645e202ed053239c974742222c76"
user_city = input("Enter name of city :")
url = f"https://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={api_key}&units=metric"
data = requests.get(url).json()
print("City name :", user_city)
print ("longitude :", data["coord"]["lon"])
print ("latitude :", data["coord"]["lat"])
print ("Temperature :", data["main"]["temp"])
print ("Humidity :", data["main"]["humidity"])
print ("description :", data["weather"][0]["description"])