from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.template import loader


def send_email_touser(email,user,user_dict):
    # import pdb
    # pdb.set_trace()
    subject = 'TEST MAIL'
    message = f'Hi {user}, thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    template=loader.get_template("F://PYTHON//Django//Django_Rest_Demo//demo_project11//email_app//templates//email_temp.html")
    temp_data={"temp":user_dict}
    html_file=template.render(temp_data)
    # obj=send_mail(subject, message, email_from, recipient_list)
    obj=EmailMessage(subject, html_file, email_from, recipient_list)
    obj.content_subtype="html"
    obj.send()
    print("*******************",obj)
