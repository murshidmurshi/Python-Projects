import requests

API_KEY="cb74ca90c3dcc5bfd77d529613786511"
BASE_URL="http://api.openweathermap.org/data/2.5/weather"


city=input('enter the city: ')

requests_url=f"{BASE_URL}?appid={API_KEY}&q={city}"

response=requests.get(requests_url)


if response.status_code==200:
    data=response.json()
    weather=data["weather"][0]["description"]
    temprature=round(data["main"]["temp"]-273.15,2)
    print("weather:",weather)
    print("temprature:",temprature,'celcius')

else:
    print('sss')