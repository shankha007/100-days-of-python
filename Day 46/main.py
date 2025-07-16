from bs4 import BeautifulSoup
import requests
import env
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=env.REDIRECT_URI,
        client_id=env.CLIENT_ID,
        client_secret=env.CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="31q3htvjnrhoo6hihaanxbivl3wu"
    )
)
user_id = sp.current_user()["id"]

user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{user_date}/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

response = requests.get(url=BILLBOARD_URL, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [item.getText().strip() for item in song_names_spans]

song_uris = []
year = user_date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        # print(f"{song} doesn't exist in Spotify. Skipped.")
        pass

playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)
# print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
