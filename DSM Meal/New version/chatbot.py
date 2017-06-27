# -*-coding:utf-8

from konlpy.tag import Hannanum
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import json
import random

hannanum = Hannanum()


class Trigger:
    # trigger worlds
    weather = {"today", "weather", "know", "tomorrow", "next", "week"}  # first-class word : weather

    meal = {"cafeteria", "rice", "lunch", "dinner", "breakfast", "morning", "today", "tomorrow", "meal"}  # first-class word : "rice", "lunch", "dinner", "breakfast", "morning",

    DMS_meta = {"dormitory", "menu", "show"}
    DMS_Outing = {"outing", "going", "out", "saturday", "sunday", "both", "all"}  # first-class word : going, out //going - out couple is admitted when both are coupled in one sentences //
    DMS_Return = {"homecoming", "return", "home", "going", "leave"}  # going 은 home 이 표현된 경우에만
    DMS_Stay = {"stay" "this", "week", "residue"}  # first-class word : stay

    teacher_menu = {"teacher", "where"}

    groups = {"sinaburo", "enroboti", "a.rbt", "a.iot", "info", "hack", "d", "icc", "wce", "gram", "sapiens", "qss"}
    # TODO: organize group names.

    dummy_answer = ["ㅋㅋㅋㅋㅋㅋ", "ㅎㅎㅎㅎ", "ㅇㅋㅇㅋ", " 아하", "그런가..?", "아 몰라몰라 다음!", "난 모르겠당", "검색이라도 해주까?", "검색해볼각?"]

    ext_2Minsub_01 = {"retraction", "angle", "drop"}  # 자퇴각? / 자퇴 -> 자퇴각!


def userInput(chat_input):
    # TODO: add Exception for invalid inputs
    # TODO:Using GOOGLE Translate API, normalize expressions
    chat_input = chat_input.lower()
    nouns = hannanum.pos(chat_input)
    words = []
    for i in range(0, len(nouns)):
        words.append(nouns[i][0])

    set(words)
    print(words)
    return words


def weatherc_omponent(time):
    if time is "present":
        def present():
            url = 'http://api.openweathermap.org/data/2.5/weather'
            service_key = 'e439f48431e739fcfd6c3127c1d0d582'
            id = 1835235

            queryParams = '?' + urlencode({quote_plus('id'): id}) + '&' + urlencode(
                {quote_plus('APPID'): service_key})
            request = Request(url + queryParams)
            request.get_method = lambda: 'GET'

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

        return present()

    elif time is "today":
        return "TODAY WEATHER"

    elif time is "tomorrow":
        return "TOMORROW WEATHER"


    else:
        return "WEEK WEATHER"


def DMS_meal_component(date, time):
    #Funtional
    return "MEAL" + str(date) + str(time)
        # TODO: request to DMS meal API

    '''
    <date_> - 1 -<time> _ 0
              |         |_ 1
              |         |_ 2
              |         |_ None -- select option
              |     
              0 - <time_> (week or month // select option for user)
    ''' #DOCSTRING


def DMS_outing_component(date):
    # TODO: request DMS API by par-date
    return "GOING OUT" #Dummy


def DMS_return_component(stay, return_date, back_date):
    return "RETURN" #Dummy

trigger = Trigger()


def router(processed_text):
    intersections_meal = set(Trigger.meal).intersection(set(processed_text))
    intersections_outing = set(Trigger.DMS_Outing).intersection(set(processed_text))
    intersections_stay = set(Trigger.DMS_Stay).intersection(set(processed_text))
    intersections_return = set(Trigger.DMS_Return).intersection(set(processed_text))
    intersections_meta = set(Trigger.DMS_meta).intersection(set(processed_text))


    if "weather" in set(processed_text):
        if "today" in (set(Trigger.weather).intersection(set(processed_text))):
            return weatherc_omponent("today")
        elif "tomorrow" in (set(Trigger.weather).intersection(set(processed_text))):
            return weatherc_omponent("tomorrow")
        elif "next" in (set(Trigger.weather).intersection(set(processed_text))) or "week" in (set(Trigger.weather).intersection(set(processed_text))):
            return weatherc_omponent("week")
        else:
            if random.randrange(0, 2) == 1:
                return weatherc_omponent("today")
            else:
                return weatherc_omponent("week")


    elif ("rice" in intersections_meal) or ("meal" in intersections_meal) or ("cafeteria" in intersections_meal):
        if "today" in intersections_meal:
            if "breakfast" in intersections_meal:
                return DMS_meal_component("today", 0)
                # TODO: Meal DB Parse module - today (naming : DMSMeal(date, time)
            elif "lunch" in intersections_meal:
                return DMS_meal_component("today", 1)
            elif "dinner" in intersections_meal:
                return DMS_meal_component("today", 2)
            else:
                if random.randrange(0, 2) == 1:
                    return DMS_meal_component("today", None)
                else:
                    #TODO: request to user
                    return DMS_meal_component("today", None)
        else:
            return DMS_meal_component(None, None)

    elif "breakfast" in intersections_meal:
        return DMS_meal_component("today", 0)
    elif "lunch" in intersections_meal:
        return DMS_meal_component("today", 1)
    elif "dinner" in intersections_meal:
        return DMS_meal_component("today", 2)

    elif ("outing" in intersections_outing) or (("going" in intersections_outing) and ("out" in intersections_outing)):
        # TODO: confirm message to user when else statement
        if ("saturday" in intersections_outing) and ("sunday" not in intersections_outing):
            return DMS_outing_component(0)
        elif ("saturday" not in intersections_outing) and ("sunday" in intersections_outing):
            return DMS_outing_component(1)
        elif ("saturday" in intersections_outing) and ("sunday" in intersections_outing) or ("all" in intersections_outing) or ("both" in intersections_outing):
            return DMS_outing_component(2)
        else:
            # request to user
            return DMS_outing_component(None)

    elif ("homecoming" in intersections_return) or ("return" in intersections_return) or (("return" in intersections_return) and ("home" in intersections_return)) or (("going" in intersections_return) and ("home" in intersections_return)) or ("leave" in intersections_return):
        # TODO: request options to user
        select = {"return": None, "back": None}
        return DMS_return_component(True, select["return"], select["back"])

    elif ("stay" in intersections_stay) or ("residue" in intersections_stay):
        if ("this" in intersections_stay) and ("weekend" in intersections_stay):
            return DMS_return_component(False, None, None)
        else:
            #TODO: announce to user that we can do it only this week and request
            return DMS_return_component(False, None, None)

    elif ("dormitory" in intersections_meta) or (("menu" in intersections_meta) and ("show" in intersections_meta)):
        select = 99
        #TODO: show menu and select menu
        print("DORMITORY SYSTEM")
        if select == 0:
            option = 99
            #TODO: select date 0, 1, 2
            return DMS_outing_component(option)
        elif select == 1:
            option = {"return": None, "back": None}
            return DMS_return_component(True, option["return"], option["back"])
        else:
            # ask one more
            # TODO: show menu and select menu

            if select == 0:
                option = 99
                # TODO: select date 0, 1, 2
                return DMS_outing_component(option)
            elif select == 1:
                option = {"return": None, "back": None}
                return DMS_return_component(True, option["return"], option["back"])
            else:
                return 0
    else:
        if "tmdrjf01" in set(processed_text):
            return "그는... 체고.... tmdrjf01은 체고...!"

        elif ("자퇴" in set(processed_text)) or ("자퇴각" in set(processed_text)):
            option = random.randrange(0, 4)
            if option == 0:
                return "자퇴각?"
            else:
                return "유성신경정신과의원 - 신성동 · 042-823-8275 \n 은빛사랑정신과의원 - 월평1동 427 · 042-486-2800"

        elif "젠카이노" in set(processed_text):
            return "아이도루마스타!!"

        #추가바람
        else:
            select = random.randint(0, len(Trigger.dummy_answer) - 1)
            return Trigger.dummy_answer[select]


print(router(userInput(input(">>>"))))


