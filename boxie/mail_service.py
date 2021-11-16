import smtplib, ssl, database

port = 465  # For SSL
password = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" #removed

# Create a secure SSL context
context = ssl.create_default_context()

sender_email = "boxie.do.not.reply@gmail.com"
receiver_email = "boxie.do.not.reply@gmail.com"
message = """\
Subject: Attention! Box has been unlocked!

Dear staff! 

The box has been unlocked by courier.
Please check circumstances.

Best regards,
Boxie security team."""


message2 = """\
Subject: Attention! Pin has been changed!

Dear staff! 

The PIN of the box has been changed by courier.

Please check circumstances.

Best regards,
Boxie security team."""

def send_security_message_box_unlocked():
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("boxie.do.not.reply@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)

def send_security_message_pin_changed():
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("boxie.do.not.reply@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message2)

