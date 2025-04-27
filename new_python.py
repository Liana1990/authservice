import smtplib
from email.message import EmailMessage

def send_email(to_email, subject, body):
    # Email account credentials
    from_email = "goldnsip@gmail.com" #cragir@ pet qe unena email, voric petq e userin code uxarkel, vor vstah linenq vor chisht user e
    app_password = ""  #to do  Use App Password, not your Gmail password!

    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(body)

    # Connect to Gmail SMTP server and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(from_email, app_password)
        smtp.send_message(msg)

#todo send_email("samvel.arakelyan00@gmail.com", "Password Reset", "Click here to reset your password.")