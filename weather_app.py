import requests
import json
city=input("enter the city to search the weather of that perticular place: ")
url=f"https://api.weatherapi.com/v1/current.json?key=69747b404f724c8392f100014240804&q={city}"

r=requests.get(url)
wdic=json.loads(r.text)
print(f"{wdic["current"]}")
