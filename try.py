from flask import Flask
from flask_mail import Mail, Message
import os
import sys

app = Flask(__name__)

mail_settings = {
  "MAIL_SERVER" : 'smtp.gmail.com',
  "MAIL_USE_TLS" : False,
  "MAIL_USE_SSL" : True,
  "MAIL_PORT" : 465,
  "MAIL_USERNAME" : 'your-mail',
  "MAIL_PASSWORD" : 'your-password'
}

app.config.update(mail_settings)
mail = Mail(app)

if __name__ == '__main__':
    print("------------------------------------------------------------------------------------------------------")
    recipients_email = input("Sending Email To : ")
    recipients_username = input("Username : ")
    subject = input("Subject Of Conversation : ")
    message = input("Your Message : ")
    try:
        with app.app_context():
            msg = Message(sender=app.config.get("MAIL_USERNAME"),
                          recipients = [recipients_email]
            )
            msg.subject = subject
            msg.html = "Hi " + recipients_username + "," + "<br>" + message
            mail.send(msg)
            print("------------------------------------------------------------------------------------------------------")
            print("Sending 1%")
            print("Sending 15%")
            print("Sending 30%")
            print("Sending 50%")
            print("Sending 100%")
            print("Message Sent.")
            print("------------------------------------------------------------------------------------------------------")
    except:
        print("------------------------------------------------------------------------------------------------------")
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("------------------------------------------------------------------------------------------------------")