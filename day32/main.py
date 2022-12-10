# Day 32 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Send Email (smtplib) & Manage Dates (datetime) - Automated Birthday Wisher

from datetime import datetime
import pandas
import random
import smtplib
from info import *

today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("./birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        # print(contents)

    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        # connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
        # print(msg)