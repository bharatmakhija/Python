# Sending emails using smtp library

- I am using smtplib for this, this is a python lib which is used to send emails
- It comes default with python package so we don't have to pip install this one

## How to handle 2 factor authentication in case of Gmail

[L1]: https://security.google.com/settings/security/apppasswords

- Log-in into Gmail with your account   
- Navigate to [Google Secutiry][L1] 
- In 'select app' choose 'custom', give it an arbitrary name and press generate
- It will give you 16 chars token.

# SampleCode

```python
import smtplib

email_domain = 'smtp.gmail.com'
port = 587
from_user = '' # keep sender email here
passe = '****************' # This pass is required for login which has added security like 2 factor authentication 
to_user = '' # keep email to which we want to sent the message
server = smtplib.SMTP(email_domain, port)
server.starttls()
try:
    server.login(from_user,passe)
except Exception as e:
    print(e)
message = "Hi there!! sending this mail from python.." # some message to send in body
try:
    server.sendmail(from_user,to_user, message)
    print("Mail sent successfully to " + to_user)
except Exception as e:
    print("sending failed! could not send email due to following error")
    print(e)
```

