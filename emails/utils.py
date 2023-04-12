import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import From, To, Subject, PlainTextContent, HtmlContent, Mail, Content
import urllib.request as urllib
from django.template.loader import render_to_string
import threading
from django import template


#SENDGRID_CLIENT = SendGridAPIClient(api_key='')
#FROM_EMAIL = "cto@conveyuall.com"


class EmailThread(threading.Thread):
    # def __init__(self, email):
    #     self.email = email
    #     threading.Thread.__init__(self)

    # def run(self):
    #     try:
    #         response = SENDGRID_CLIENT.send(message=self.email)

    #     except urllib.HTTPError as e:
    #         print(e.read())
    #         exit()
    pass


def send_email(email_type, subject, recipients, object=None, *args, **kwargs):
    # if email_type == "user_verification_email":
    #     user = object

    #     user_verification_context = {
    #         "user": user,
    #         "token":kwargs.get("token")
    #     }


    #     plain_message = render_to_string('email_templates/user_verify_email.txt',
    #                                      user_verification_context)

    #     # html message
    #     html_message = render_to_string('email_templates/user_verify_email.html',
    #                                     user_verification_context)
        
   
    # to_email = To(recipients)

    # subject = Subject(subject)

    # html_content = HtmlContent(html_message)

    # plain_text_content = Content("text/plain", plain_message)

    #email = Mail(FROM_EMAIL, to_email, subject, plain_text_content, html_content)

    #EmailThread(email).start()
    pass
