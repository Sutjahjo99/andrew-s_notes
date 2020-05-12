from flask_mail import Message
from flaskblog import mail


def send_email(useremail, usertitle, usermess):

    msg = Message(f'andrewnotes.com Contact: {usertitle}', sender=useremail, recipients=["andrewowen1991@gmail.com"])
    msg.body = f'From: {useremail}\n--------------------------------\n{usermess}'

    mail.send(msg)