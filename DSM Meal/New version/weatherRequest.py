from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import json

def getWeather():
    url = 'http://api.openweathermap.org/data/2.5/weather'
    service_key = 'e439f48431e739fcfd6c3127c1d0d582'
    id = 1835235

    queryParams = '?' + urlencode({quote_plus('id'): id}) + '&' + urlencode({quote_plus('APPID'): service_key})
    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()

    response_body = (urlopen(request).read()).decode("utf-8")

    WeatherData = json.loads(response_body)

    # 파싱을 실행하는 부분입니다. JSON 변환 후 리스트 슬라이싱을 사용했습니다
    weather = WeatherData['weather'][0]
    weather = weather['id']

    temp_min = WeatherData['main']['temp_min'] - 273.15
    temp_max = WeatherData['main']['temp_max'] - 273.15
    avertemp = (temp_max + temp_min) / 2

    humidity = WeatherData['main']['humidity']

    pressure = WeatherData['main']['pressure']

    temp = WeatherData['main']['temp'] - 273.15

    return temp, temp_max, temp_min, humidity
