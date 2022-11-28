import smtplib

my_email = "b34ux.100days.test@gmail.com"
password = "zkhmnvdeagjgtixv"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="beaux.walton@gmail.com", 
        msg="Subject:Hello\n\nThis is the body of my bad ass email."
    )