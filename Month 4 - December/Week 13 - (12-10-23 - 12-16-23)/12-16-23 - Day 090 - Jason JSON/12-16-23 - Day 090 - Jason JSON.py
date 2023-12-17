import requests
import json
import urllib

def get_random_users(num_users=10):
  url = f"https://randomuser.me/api/?results={num_users}"
  response = requests.get(url)
  data = response.json()
  return data['results']

def save_profile_pics(users):
  for user in users:
    first_name = user['name']['first']
    last_name = user['name']['last']
    image_url = user['picture']['medium']

    image_filename = f"{first_name} {last_name}.jpg"
    urllib.request.urlretrieve(image_url, image_filename)
    print(f"Saved {image_filename}")

random_users = get_random_users()

save_profile_pics(random_users)