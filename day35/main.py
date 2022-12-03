import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = os.environ.get("OWM_API_KEY")
units = "metric"
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

weather_params = {
    "lat": 49.122690,
    "lon": -122.704720,
    "appid": api_key,
    "units": units,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

will_rain = False

#Had to modify the exercise here because the OpenWeather API access changed.
condition_code = weather_data["weather"][0]["id"]
temperature = weather_data["main"]["temp"]

# if int(temperature) < 10:
#     print("It's an inside day.")
# elif int(condition_code) < 700:
#     will_rain = True
# else:
#     print(f"It's fine and {temperature} degrees.")

# if will_rain:

# Made a real-world app for me - "Is it too cold to go outside?"
if int(temperature) < 10:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bro, it is too cold outside for your warm Australian blood. ❄️ Forget it!",
        from_='+17207067009',
        to='+16043639155'
    )

print(message.status)