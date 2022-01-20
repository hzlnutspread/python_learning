import smtplib

sender = "smithkg293@gmail.com"
receiver = "kennyg293@hotmail.com"
password = "___"
subject = "Coding test email"
body = "I wrote an email using coding and I am sending you an email to test it"

# header
message = f"""From: Ken {sender}
To: Me {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()


try:
    server.login(sender, password)
    print("You Logged In...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")