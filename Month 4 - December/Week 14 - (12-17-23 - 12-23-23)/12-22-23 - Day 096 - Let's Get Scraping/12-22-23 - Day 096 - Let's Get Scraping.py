import requests
from bs4 import BeautifulSoup

base_url = "https://news.ycombinator.com/"

start_page = 1
end_page = 10

for page in range(start_page, end_page + 1):
    url = f"{base_url}?p={page}"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        headlines = soup.find_all("a", class_="storylink")

        count = 0

        for headline in headlines:
            if "python" in headline.text.lower() or "replit" in headline.text.lower():
                print(headline.text)
                count += 1

        if count == 0:
            print(f"No headlines found containing 'python' or 'replit' on page {page}.")
        else:
            print(f"Total headlines containing 'python' or 'replit' on page {page}: {count}")
    else:
        print(f"Failed to retrieve the page {page}. Status Code:", response.status_code)