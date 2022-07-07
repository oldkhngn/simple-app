print("Hello world")
#fetch weather api then print the temperature
import requests
import json

def getWeather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=b1b15e88fa797225412429c1c50c122a1"
    response = requests.get(url)
    data = response.json()
    return data["main"]["temp"]
print(getWeather("London"))