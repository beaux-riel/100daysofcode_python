# Day 32 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Send Email (smtplib) & Manage Dates (datetime) - Clean(er) version

# Note: I never managed to get Gmail or Yahoo working with this automation (although have done so successfully in the past.)
# Given Gmail and Yahoo's security stance, it's not surprising. Will revisit this exercise at a later date.

from info import *
import smtplib
import datetime as dt
import random

my_email = MY_EMAIL
password = PASSWORD

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("day32/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=my_email, 
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )