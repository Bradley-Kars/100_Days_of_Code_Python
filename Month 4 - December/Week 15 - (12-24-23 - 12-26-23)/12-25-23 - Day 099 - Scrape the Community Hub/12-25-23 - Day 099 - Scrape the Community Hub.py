import requests
from bs4 import BeautifulSoup
import schedule
import time
import smtplib
from email.message import EmailMessage

sender_email = "bradley.kars@gmail.com"
sender_password = "insert password"
receiver_email = "bradley.kars@gmail.com"

interesting_topics = ["Python", "Web Development"]

scraped_events = set()

def scrape_and_filter():
    global scraped_events
    url = "https://replit.com/community-hub"

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        events = soup.find_all('a', class_='event-card')

        filtered_events = [event for event in events if any(topic.lower() in event.text.lower() for topic in interesting_topics)]

        new_events = [event for event in filtered_events if event['href'] not in scraped_events]

        if new_events:
            send_email(new_events)
            scraped_events.update(event['href'] for event in new_events)

    except requests.RequestException as e:
        print(f"Error scraping events: {e}")

def send_email(new_events):
    subject = "New Replit Community Events of Interest"
    body = "Check out these new events:\n\n"
    for event in new_events:
        body += f"{event.text.strip()}\n{event['href']}\n\n"

    message = EmailMessage()
    message.set_content(body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        print("Email sent successfully")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

schedule.every(6).hours.do(scrape_and_filter)

while True:
    schedule.run_pending()
    time.sleep(1)