import json
import requests

def cWeather() :
    params = {"version": "1", "city":"대전", "county":"유성구","village":"장동"}
    headers = {"appKey": "b4bdaadc-32c7-3797-98ba-4482d1093173"}
    weather_request = requests.get("http://apis.skplanetx.com/weather/current/hourly", params=params, headers=headers)

    data = json.loads(weather_request.text)
    weather = data["weather"]["hourly"]
    cTime = weather[0]["timeRelease"]
    cSky = weather[0]["sky"]["name"]
    cWind = str(round(float(weather[0]["wind"]["wspd"]), 1))
    cTemp = str(round(float(weather[0]["temperature"]["tc"]), 1))
    weather = '현재 하늘은 ' +cSky+ ', 풍속은'  +cWind+ 'm/s, 기온은 ' +cTemp+ '도 입니다.'
    
    return weather
