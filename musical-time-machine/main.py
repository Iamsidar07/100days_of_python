import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIFY_CLIENT_ID = os.environ.get(["SPOTIFY_CLIENT_ID"])
SPOTIFY_CLIENT_SECRET = os.environ.get(["SPOTIFY_CLIENT_SECRET"])

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri="http://example.com",
    scope="playlist-modify-private",
    username="Manoj Kumar",
    cache_path="token.txt",
    show_dialog=True
))

desired_date = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{desired_date}"

response = requests.get(URL)
html_contents = response.text
soup = BeautifulSoup(html_contents, "html.parser")
songs = soup.select("li ul li h3")
song_titles = [song.getText().strip() for song in songs]

USER_ID = sp.current_user()["id"]

song_uris = []
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{desired_date.split('-')[0]}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} not found.")

PLAYLIST_NAME = f"{desired_date} Billboard 100"


playlist = sp.user_playlist_create(
    name=PLAYLIST_NAME,
    user=USER_ID,
    public=False,
    description="100 billboard"
)

PLAYLIST_ID = playlist["id"]

result = sp.playlist_add_items(
    playlist_id=PLAYLIST_ID,
    items=song_uris
)
