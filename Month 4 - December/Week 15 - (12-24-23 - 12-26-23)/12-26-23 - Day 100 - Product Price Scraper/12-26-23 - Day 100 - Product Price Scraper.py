import re
import smtplib
from scrapingbee import ScrapingBeeClient

api_key = 'you_api_key'

sender_email = "email"
receiver_email = "email"
email_password = "password"

url = "https://www.amazon.com/PlayStation%C2%AE5-Digital-slim-PlayStation-5/dp/B0CL5KNB9M"

client = ScrapingBeeClient(api_key=api_key)

def send_email(product_name, current_price):
    subject = "Price Drop Alert"
    body = f"The price of {product_name} has dropped below $500. The current price is {current_price}."

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()

        server.login(sender_email, email_password)

        message = f"Subject: {subject}\n\n{body.encode('utf-8')}"

        server.sendmail(sender_email, receiver_email, message)

response = client.get(
    url,
    params={
        'extract_rules': {
            "name": {
                "selector": "span[id='productTitle']",
                "output": "text",
            },
            "price": {
                "selector": "span[class='a-price a-text-price a-size-medium apexPriceToPay'] > span",
                "output": "text",
            },
            "rating": {
                "selector": "i[class='a-icon a-icon-star a-star-4-5'] > span",
                "output": "text",
            },
            "description": {
                "selector": "div[id='productDescription']",
                "output": "text",
            },
            "full_html": {
                "selector": "html",
                "output": "html",
            },
        }
    }
)

if response.ok:
    scraped_data = response.json()

    price_match = re.search(r'[\d.]+', scraped_data['price'])
    current_price = float(price_match.group()) if price_match else 0.0

    images = re.findall('"hiRes":"(.+?)"', response.json()['full_html'])

    print(scraped_data['name'])
    print(f"Current Price: {current_price}")
    print(scraped_data['rating'])
    print(scraped_data['description'])
    print(images)

    if current_price < 500:
        send_email(scraped_data['name'], current_price)
        print("Email sent! Price is below $500")
else:
    print(f"Error: {response.status_code}")
