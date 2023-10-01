import requests
from datetime import date
from cs50 import SQL

from helpers import condition_emoji, recommendation, more_info

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///cycling.db")

def weather_hourly(user=None, city="kaunas"):
    today = str(date.today())

    if user:
        temp_ranges = db.execute("SELECT low, mid, high FROM user_preferences WHERE user_id=?", user)[0]
    else:
        temp_ranges = db.execute("SELECT low, mid, high FROM default_preferences")[0]

    # getting weather for Kaunas from meterology station
    url = (f"https://api.meteo.lt/v1/places/{city}/forecasts/long-term")
    response = requests.get(url)

    # checking if there is an error from API
    if  response.status_code != 200:
        return "error"

    # no errors - then format got data as needed
    # data = response.json()["observations"]
    data = response.json()["forecastTimestamps"]
    newData = [{ "day" : item["forecastTimeUtc"].split(' ')[0],
                    "time": item["forecastTimeUtc"].split(' ')[1][:5],
                    "airTemp": item["airTemperature"],
                    "conditions": condition_emoji(item["conditionCode"]),
                    "recommendation": recommendation(item["airTemperature"], item["conditionCode"], temp_ranges),
                    "info": more_info(item["airTemperature"], temp_ranges)
                    } for item in data]
    filteredData = [item for item in newData if item["day"] == today]

    return filteredData