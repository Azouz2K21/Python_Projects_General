import smtplib
from email.message import EmailMessage

def email_alert(subject , body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    
    email_user = "mo1122000azouz@gmail.com"
    msg['from'] = email_user
    user_pass = "lilqlzlwcyycetqv"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_user, user_pass)
    server.send_message(msg)
    server.quit()

email_user = "mo1122000azouz@gmail.com"
if __name__ == '__main__':
    email_alert("subject" , "body", "mo1122000azouz@gmail.com")
    print("message sent to "+ email_user)

