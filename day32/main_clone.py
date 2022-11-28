# import smtplib
# from info import *

# # Google (didn't work)
# # my_email = "b34ux.100days.test@gmail.com"
# # password = "zkhmnvdeagjgtixv"

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

print(type(year))