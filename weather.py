import pyowm
from datetime import datetime, timedelta

owm = pyowm.OWM('5b6380a48fa6da05fbd15f3f2b34635a')

def format_time(time):
    return time.strftime('%Y-%m-%d %H:%M:%S')

def get_weather_forecast(lat, log):
    fc = owm.three_hours_forecast_at_coords(lat,log)
    f = fc.get_forecast()
    if len(f) == 0:
        return None
    now = datetime.now()

    forecast = []
    for weather in f:
        time = datetime.fromtimestamp(weather.get_reference_time('unix'))
        if time - now < timedelta(days = 1):
            forecast.append({"time": time,"status":weather.get_detailed_status()})
        else:
            break
    return forecast

def display_forecast(forecast):
    for f in forecast:
        print(format_time(f['time']),f['status'])

if __name__ == "__main__":
    forecast = get_weather_forecast(42.4851,-71.4328)
    display_forecast(forecast)
