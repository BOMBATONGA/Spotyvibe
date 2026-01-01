import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
from flask import session


def create_auth_manager():
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
        cache_handler=spotipy.cache_handler.FlaskSessionCacheHandler(session),
        show_dialog=True
    )

    #attain scope
    return auth_manager

def fetch_data():
    print("Initializing...")
    auth_manager = create_auth_manager()

    token_dict = auth_manager.validate_token(auth_manager.get_cached_token())
    if not token_dict:
        return None

    #get user scope
    sp = spotipy.Spotify(auth=token_dict['access_token'])
    print("Scope attained!")

    #get data from scope
    print("Fetching data...")
    user_info = sp.current_user()
    saved_tracks_short = sp.current_user_top_tracks(limit=25, time_range="short_term")
    saved_tracks_medium = sp.current_user_top_tracks(limit=25, time_range="medium_term")
    saved_tracks_long = sp.current_user_top_tracks(limit=25, time_range="long_term")
    saved_artists_short = sp.current_user_top_artists(limit=25, time_range="short_term")
    saved_artists_medium = sp.current_user_top_artists(limit=25, time_range="medium_term")
    saved_artists_long = sp.current_user_top_artists(limit=25, time_range="long_term")
    print("Data attained!")

    #print recent save tracks + albums
    res = "\nUSER DATA:"
    res += "\nTOP TRACKS SHORT TERM (4 WEEKS)"
    for idx, track in enumerate(saved_tracks_short['items']):
        res += track['artists'][0]['name'] + " - " + track['name']
    res += "\nTOP TRACKS MEDIUM TERM (6 MONTHS)"
    for idx, track in enumerate(saved_tracks_medium['items']):
        res += track['artists'][0]['name'] + " - " + track['name']
    res += "\nTOP TRACKS LONG TERM (1 YEAR)"
    for idx, track in enumerate(saved_tracks_long['items']):
        res += track['artists'][0]['name'] + " - " + track['name']

    res += "\nTOP ARTISTS SHORT TERM (4 WEEKS)"
    for idx, artist in enumerate(saved_artists_short['items']):
        res += artist['name']
    res += "\nTOP ARTISTS MEDIUM TERM (6 MONTHS)"
    for idx, artist in enumerate(saved_artists_medium['items']):
        res += artist['name']
    res += "\nTOP ARTISTS LONG TERM (1 YEAR)"
    for idx, artist in enumerate(saved_artists_long['items']):
        res += artist['name']
    res += "\nUSERNAME: " + user_info.get('display_name')
    return res