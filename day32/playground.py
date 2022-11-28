import smtplib

my_email = "b34ux.100days.test@gmail.com"
password = "iqlrftwwhbftnzyh"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="contact@stellaverona.com", msg="Hello")
connection.close()