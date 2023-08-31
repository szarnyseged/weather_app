import requests
import json
import datetime
import os
from tkinter import messagebox


# source: https://openweathermap.org/current
# example geo: http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={API key}
# example: https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API key}
URL_GEO_LOCATION = "http://api.openweathermap.org/geo/1.0/direct"
URL_CURRENT_WEATHER = "https://api.openweathermap.org/data/2.5/weather"
URL_FORECAST = "https://api.openweathermap.org/data/2.5/forecast"

try:
    with open("./api_key.txt", "r") as source_file:
        for sor in source_file:
            API_KEY = sor.strip()
except FileNotFoundError:
    messagebox.showerror("file not found", 
                         "api-key not found.\n" \
                            "1. create your api-key at https://openweathermap.org \n" \
                            "2. create api_key.txt to main folder and paste your key \n" \
                            "3. done" \
                        )


def get_geo_location(city_name, country_code=None):
    """
    returns (latitude, longitude)
    required for other requests
    """

    if country_code != None:
        payload = {"q": city_name + ", " + country_code, "appid": API_KEY}
    else:
        payload = {"q": city_name, "appid": API_KEY}
    resp = requests.get(URL_GEO_LOCATION, params=payload)
    resp.encoding = "UTF-8"
    resp = resp.json()
    if len(resp) == 0:
        messagebox.showwarning("ValueError", "Nem találtunk ilyen nevű várost")
        #raise ValueError("no city found with this name in database")
    return resp[0]["lat"], resp[0]["lon"]




def get_current_weather(city_name, country_code=None):
    """
    get current weather of a city
    uses get_geo_location()
    returns a json content
    """

    lat, lon = get_geo_location(city_name, country_code)
    payload = {"lat": lat, "lon": lon, "units": "metric", "lang": "hu", "appid": API_KEY}
    resp = requests.get(URL_CURRENT_WEATHER, params=payload)
    resp.encoding = "UTF-8"
    resp = resp.json()

    # create file with data
    with open("./data/last_data.json", "w") as celfajl:
        json.dump(resp, celfajl, indent=3, ensure_ascii=False)
    convert_current_weather(resp)
    # works, but no popup
    # os.system(r".\data\last_data_converted.json")
    # os.startfile(".\data\last_data_converted.json")
    return resp


def convert_current_weather(data_json):
    """
    convert current weather data to more readable version.
    new file is located: data/last_data_converted.json
    """

    data_json["main"]["temp"] = str(data_json["main"]["temp"]) + " C°"
    data_json["main"]["feels_like"] = str(data_json["main"]["feels_like"]) + " C°"
    data_json["main"]["temp_min"] = str(data_json["main"]["temp_min"]) + " C°"
    data_json["main"]["temp_max"] = str(data_json["main"]["temp_max"]) + " C°"
    data_json["main"]["humidity"] = str(data_json["main"]["humidity"]) + " %"
    data_json["visibility"] = str(data_json["visibility"]) + " meters"
    data_json["dt"] = str(datetime.datetime.fromtimestamp(data_json["dt"]))
    data_json["sys"]["sunrise"] = str(datetime.datetime.fromtimestamp(data_json["sys"]["sunrise"]))
    data_json["sys"]["sunset"] = str(datetime.datetime.fromtimestamp(data_json["sys"]["sunset"]))
    data_json["timezone"] = str(datetime.timedelta(seconds=data_json["timezone"])) + " (shift from UTC)"


    # create readable file
    with open("./data/last_data_converted.json", "w") as celfajl:
        json.dump(data_json, celfajl, indent=3, ensure_ascii=False)


def get_five_day_forecast(city_name, country_code=None):
    lat, lon = get_geo_location(city_name, country_code)
    payload = {"lat": lat, "lon": lon, "appid": API_KEY, "units": "metric", "lang": "hu"}
    resp = requests.get(URL_FORECAST, params=payload)
    resp.encoding = "UTF-8"
    resp = resp.json()

    # create file with data
    with open("./data/last_data.json", "w") as celfajl:
        json.dump(resp, celfajl, indent=3, ensure_ascii=False)
    convert_five_day_forecast(resp)
    # os.system(r".\data\last_data_converted.json")
    return resp


def convert_five_day_forecast(data_json):
    """
    convert five day forecast data to more readable version.
    new file is located: data/last_data_converted.json
    """

    for index in range(len(data_json["list"])):
        data_json["list"][index]["main"]["temp"] = str(data_json["list"][index]["main"]["temp"]) + " C°"
        data_json["list"][index]["main"]["feels_like"] = str(data_json["list"][index]["main"]["feels_like"]) + " C°"
        data_json["list"][index]["main"]["temp_min"] = str(data_json["list"][index]["main"]["temp_min"]) + " C°"
        data_json["list"][index]["main"]["temp_max"] = str(data_json["list"][index]["main"]["temp_max"]) + " C°"
        data_json["list"][index]["main"]["humidity"] = str(data_json["list"][index]["main"]["humidity"]) + " %"
        data_json["list"][index]["visibility"] = str(data_json["list"][index]["visibility"]) + " meters"
    
    data_json["city"]["sunrise"] = str(datetime.datetime.fromtimestamp(data_json["city"]["sunrise"]))
    data_json["city"]["sunset"] = str(datetime.datetime.fromtimestamp(data_json["city"]["sunset"]))
    data_json["city"]["timezone"] = str(datetime.timedelta(seconds=data_json["city"]["timezone"])) + " (shift from UTC)"

    # create readable file
    with open("./data/last_data_converted.json", "w") as celfajl:
        json.dump(data_json, celfajl, indent=3, ensure_ascii=False)


