import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import requests

def get_random_quote():
    response = requests.get("https://api.quotable.io/quotes/random")
    if response.status_code == 200:
        quote_data = response.json()
        if isinstance(quote_data, list) and quote_data:
            quote_data = quote_data[0]
        return quote_data.get("content", ""), quote_data.get("author", "")
    else:
        return None, None

def send_email(quote, author):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "bradley.kars@gmail.com"
    password = "insert password here"
    recipient_email = "bradley.kars@gmail.com"

    subject = "Daily Motivational Quote"
    body = f"Here's your daily motivational quote:\n\n{quote}\n\n- {author}"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, message.as_string())

quote, author = get_random_quote()

if quote and author:
    send_email(quote, author)
    print("Email sent successfully!")
else:
    print("Error fetching quote. Please try again later.")