import info
import smtplib
import datetime as dt
import random

my_email = info.MY_EMAIL
password = info.PASSWORD

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
            msg=f"Subject:Monday Motivation\n\n{quote}")