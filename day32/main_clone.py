# import smtplib

# # Google (didn't work)
# my_email = "b34ux.100days.test@gmail.com"
# password = "iqlrftwwhbftnzyh"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="beaux.walton@gmail.com", msg="Hello")
# connection.close()


# import smtplib
# from info import *

# # Yahoo
# my_email = MY_EMAIL
# password = PASSWORD

# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="beaux.walton@gmail.com", 
#         msg="Subject:Hello\n\nThis is the body of my bad ass email."
#     )


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year= 1985, month= 8, day= 8, hour=17, minute=31)
print(date_of_birth)