from read import get_user_data, create_gmail_service
from weather import get_weather_forecast, display_forecast
from reversegeocode import reverse_geocode
if __name__ == "__main__":
    gmail = create_gmail_service()
    user_data = get_user_data(gmail)
    
    for data in user_data:
        print(data['sender_id'])
        lat, log = data['lat'],data['long']
        forecast = get_weather_forecast(lat,log)
        location = reverse_geocode(lat, log)
        print(location)
        display_forecast(forecast)
