from flask import Flask, render_template, request
import requests
import os
import base64
import time

app = Flask(__name__)

clientID = os.environ['CLIENT_ID']
clientSecret = os.environ['CLIENT_SECRET']

def get_access_token():
    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type": "client_credentials"}
    headers = {
        "Authorization": f"Basic {base64.b64encode(f'{clientID}:{clientSecret}'.encode()).decode()}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        access_token = response.json().get("access_token")
        expiration_time = time.time() + response.json().get("expires_in", 3600)  # Default to 1 hour
        print(f"Access Token: {access_token}, Expires in: {expiration_time} seconds")
        return access_token, expiration_time
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None, None

spotify_url = "https://api.spotify.com/v1/"
accessToken, expirationTime = get_access_token()

def get_top_songs(year, accessToken):
    search_url = f"{spotify_url}search"
    params = {
        "q": f"year:{year}",
        "type": "track",
        "limit": 10,
    }
    headers = {
        "Authorization": f"Bearer {accessToken}"
    }

    response = requests.get(search_url, params=params, headers=headers)

    if response.status_code == 200:
        songs = response.json().get("tracks", {}).get("items", [])
        return songs
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    global accessToken, expirationTime

    if expirationTime is None or time.time() > expirationTime:
        accessToken, expirationTime = get_access_token()

    if request.method == 'POST':
        year = request.form['year']
        songs = get_top_songs(year, accessToken)
        return render_template('index.html', songs=songs, year=year)
    return render_template('index.html', songs=None, year=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)