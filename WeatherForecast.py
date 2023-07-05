import requests
import datetime as dt

city_name=input("Enter city: ")

weather_data=requests.get(f" http://api.weatherapi.com/v1/current.json?key=4e7fc599ebd647cbb1f182756230407&q="+ city_name+"&aqi=no")

print(weather_data.json())
weather=weather_data.json()['current']['condition']
temp=weather_data.json()['current']

print(f"The weather in {city_name} is: {weather}")
print(f"The Temperature in {city_name} is: {temp}")