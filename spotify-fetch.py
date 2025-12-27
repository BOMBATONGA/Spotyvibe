import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

def get_scope():
    #get env variables
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

    #specify oauth
    auth_manager = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="user-library-read",
        show_dialog=True
    )

    #attain scope
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp


load_dotenv(override=True)
print("Initializing...")

sp = get_scope()
print("Scope attained")

saved_tracks = sp.current_user_saved_tracks(limit=50)
saved_albums = sp.current_user_saved_albums(limit=50)
print("\nTRACKS")
for idx, item in enumerate(saved_tracks['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " - ", track['name'])
print("\nALBUMS")
for idx, item in enumerate(saved_albums['items']):
    track = item['album']
    print(idx, track['artists'][0]['name'], " - ", track['name'])