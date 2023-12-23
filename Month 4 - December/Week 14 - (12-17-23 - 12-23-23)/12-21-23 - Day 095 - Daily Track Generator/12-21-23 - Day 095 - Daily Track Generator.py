import requests
from bs4 import BeautifulSoup
from summa import keywords
import spotipy
from spotipy.oauth2 import SpotifyOAuth

newsapi_key = "newsapi"
spotify_client_id = "spotify_id"
spotify_client_secret = "spotify_secret"


def get_news():
    country = "us"
    news_url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsapi_key}"
    news_result = requests.get(news_url)
    news_data = news_result.json()

    headlines = [article['title'] for article in news_data['articles']]
    return headlines

def generate_track_summaries(headlines):
    return [headline.split()[:2] for headline in headlines]

def search_spotify(prompt_words):
    sp_oauth = SpotifyOAuth(
    client_id=spotify_client_id,
    client_secret=spotify_client_secret,
    redirect_uri="http://localhost:8080/callback",
    cache_path=".cache",
    )
    
    token_info = sp_oauth.get_cached_token()

    if not token_info:
        token_info = sp_oauth.get_access_token()

    sp = spotipy.Spotify(auth=token_info['access_token'])

    tracks = []
    for words in prompt_words:
        query = " ".join(words)
        result = sp.search(q=query, type='track', limit=1)
        if result['tracks']['items']:
            track_name = result['tracks']['items'][0]['name']
            track_url = result['tracks']['items'][0]['external_urls']['spotify']
            tracks.append((track_name, words, track_url))

    return tracks

def display_tracks(tracks):
    for i, (track_name, prompt_words, track_url) in enumerate(tracks, start=1):
        print(f"\nTrack {i}:")
        print(f"News Headline: {' '.join(prompt_words)}")
        print(f"Song Name: {track_name}")
        print(f"Spotify URL: {track_url}\n")

def main():
    headlines = get_news()
    prompt_words = generate_track_summaries(headlines)
    tracks = search_spotify(prompt_words)
    display_tracks(tracks)

if __name__ == "__main__":
    main()