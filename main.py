from read import get_user_data, create_gmail_service
from weather import get_weather_forecast, format_forecast
from reversegeocode import reverse_geocode
import requests

MARVIN_ENDPOINT = "https://marvin-assistant.herokuapp.com/dw"

def send_weather_data(sender_id, location, forecast):
    forecast = format_forecast(forecast)
    data = {
        "sender_id": sender_id,
        "location": location,
        "forecast": forecast,
    }
    r = requests.post(url = MARVIN_ENDPOINT, data = data)
    print(r)

def process_weather_data():
    gmail = create_gmail_service()
    user_data = get_user_data(gmail)
    for data in user_data:
        lat, log = data['lat'],data['long']
        forecast = get_weather_forecast(lat,log)
        location = reverse_geocode(lat, log)
        send_weather_data(data['sender_id'], location, forecast)

if __name__ == "__main__":
    process_weather_data()
