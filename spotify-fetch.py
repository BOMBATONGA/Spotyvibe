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
        scope="user-library-read user-top-read",
        show_dialog=True
    )

    #attain scope
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp

#load env
load_dotenv(override=True)
print("Initializing...")

#get user scope
sp = get_scope()
print("Scope attained")

#get data from scope
print("Fetching data")
saved_tracks_short = sp.current_user_top_tracks(limit=25, time_range="short_term")
saved_tracks_medium = sp.current_user_top_tracks(limit=25, time_range="medium_term")
saved_tracks_long = sp.current_user_top_tracks(limit=25, time_range="long_term")
saved_artists_short = sp.current_user_top_artists(limit=25, time_range="short_term")
saved_artists_medium = sp.current_user_top_artists(limit=25, time_range="medium_term")
saved_artists_long = sp.current_user_top_artists(limit=25, time_range="long_term")
user_data = sp.current_user()
print("Data attained")

#print recent save tracks + albums
print("\nTOP TRACKS SHORT TERM (4 WEEKS)")
for idx, track in enumerate(saved_tracks_short['items']):
    print(idx + 1, track['artists'][0]['name'], " - ", track['name'])
print("\nTOP TRACKS MEDIUM TERM (6 MONTHS)")
for idx, track in enumerate(saved_tracks_medium['items']):
    print(idx + 1, track['artists'][0]['name'], " - ", track['name'])
print("\nTOP TRACKS LONG TERM (1 YEAR)")
for idx, track in enumerate(saved_tracks_long['items']):
    print(idx + 1, track['artists'][0]['name'], " - ", track['name'])

print("\nTOP ARTISTS SHORT TERM (4 WEEKS)")
for idx, artist in enumerate(saved_artists_short['items']):
    print(idx + 1, artist['name'])
print("\nTOP ARTISTS MEDIUM TERM (6 MONTHS)")
for idx, artist in enumerate(saved_artists_medium['items']):
    print(idx + 1, artist['name'])
print("\nTOP ARTISTS LONG TERM (1 YEAR)")
for idx, artist in enumerate(saved_artists_long['items']):
    print(idx + 1, artist['name'])