from pyowm import OWM
from pyowm.utils import timestamps
import matplotlib.pyplot as plt
import numpy as np


# ------------ getting city information-----------------

def collect_user_input():
    city = input("What city would you like to check the weather for? ")
    while not get_city_id(city)[0]:
        city = input("What city would you like to check the weather for? ")
    return city


def get_city_id(city):
    try:
        reg = owm.city_id_registry()
        list_of_tuples = reg.ids_for(city)  # possible improvement, work out how to add country
        id_of_city = list_of_tuples[0][0]
        return True, id_of_city
    except:
        print("Invalid input")
        return False, None


def get_city_long_lat(city):
    reg = owm.city_id_registry()
    city_coordinates = reg.locations_for(city)
    city_long = city_coordinates[0].lon
    city_lat = city_coordinates[0].lat
    return city_lat, city_long


def create_city_weather_object(city):
    weather = manager.weather_at_place(city).weather
    return weather


# -------------------- getting weather stats/details --------------------------

def get_temp(weather):
    temp_dict_celsius = weather.temperature('celsius')
    return temp_dict_celsius


def get_wind(weather):
    wind_dict = weather.wind(unit='miles_hour')
    return wind_dict


def get_sunrise_time(weather):
    sunrise = weather.sunrise_time(timeformat='date')
    return sunrise


def get_sunset_time(weather):
    sunset = weather.sunset_time(timeformat='date')
    return sunset


def get_forecast(city_id):
    forecast = manager.forecast_at_place(city_id, '3h')    #change to forecast_at_id() to get use id
    tomorrow = timestamps.tomorrow()  # datetime object for tomorrow
    clear_days = forecast.when_clear()
    most_rain = forecast.most_rainy()
    return most_rain, clear_days


def pollution(coordinates):                       #TODO figure out how to pull pollution data
    coi = owm.coindex_around_coords(coordinates)
    print("pollution working")


# ------------------------- display functions ----------------------------------


def display_clear_days(time_stamps):   #TODO refine loop to return just the date of clear days
    clear_days = {}
    for item in time_stamps:
        print(item.reference_time)
    return clear_days


def display_forecast(forecast):
    print(f'The day with the most rain will be: {forecast}')


def display_current(temp=None, wind=None, sunrise=None, sunset=None):
    high_temp = temp['temp_max']
    low_temp = temp['temp_min']
    wind_speed = wind['speed']
    print(
        f'Today\'s weather is: high-{high_temp}, low-{low_temp} \n'
        f'There are {wind_speed} mph winds \n'
        f'Sunrise is at {sunrise} and sunset is at {sunset}'
          )


# ------------------------ main function --------------------------------


def main():
    city = collect_user_input()
    # city_id = get_city_id(city)                    #returns tuple (boolean, id)
    coordinates = get_city_long_lat(city)            #in lat, long order
    local_weather = create_city_weather_object(city) #TODO need to check how to get data via cityID
    # temp_dict = get_temp(local_weather)            #figure out why wrong times get returned
    # wind_dict = get_wind(local_weather)
    # sunrise = get_sunrise_time(local_weather)
    # sunset = get_sunset_time(local_weather)
    # display_current(temp_dict, wind_dict, sunrise, sunset)
    forecast = get_forecast(city)
    display_forecast(forecast[0])
    pollution(coordinates)

# ---------------------globals------------------------------------


city = "Tel Aviv"
country = "UK"
api_key = "ab6599fd2d1d85464feaa88ff8bbcd99"
owm = OWM(api_key)
manager = owm.weather_manager()


main()



#use dir to see all the objects attributes
# ctrl hoover turns it into link, brings y to where method is written