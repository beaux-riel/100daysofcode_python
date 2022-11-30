# Day 33 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - API Endpoints & API Parameters - ISS Overhead Notifier

import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "b34ux.100days@yahoo.com"
MY_PASSWORD = "gavgek-fyvra7-qorviQ"
MY_LAT = 49.122690 # My Latitude
MY_LONG = -122.704720 # My Longitutde 

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your positiion is within +/- 5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_latitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split('T')[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split('T')[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    #It's dark

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
            connection = smtplib.SMTP("smtp.mail.yahoo.com")
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=MY_EMAIL, 
                msg=f"Subject:Look up!\n\nThe ISS is above you in the sky,"
            )