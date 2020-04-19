import smtplib

email_domain = 'smtp.gmail.com'
port = 587
from_user = 'bharatcool.678@gmail.com'
passe = 'trormxqtoompnsyi'
to_user = 'bharatkumarmakhija14@gmail.com'
server = smtplib.SMTP(email_domain, port)
server.starttls()
try:
    server.login(from_user,passe)
except Exception as e:
    print(e)
message = "Hi there!! sending this mail from python.."
try:
    server.sendmail(from_user,to_user, message)
    print("Mail sent successfully to " + to_user)
except Exception as e:
    print("sending failed! could not send email due to following error")
    print(e)