"""Script to combine 2 playlist from Spotify and add to a new one."""

import os
from pprint import pprint

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

SCOPE = "playlist-modify-public "
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

def get_all_tracks(playlist):
    """Get from playlist all tracks in chunks of 100 as
    the API only supports a maximum of 100 tracks per request.
    """

    tracks = []
    result = sp.playlist_items(playlist, fields='items.track.id,next', additional_types=['track'])
    tracks.extend(result['items'])

    while result['next']:
        result = sp.next(result)
        tracks.extend(result['items'])
    return set(map(lambda x: x['track']['id'], tracks))

my_pl_id = os.getenv("MY_PLAYLIST_ID")
my_tracks = get_all_tracks(my_pl_id)

your_pl_id = os.getenv("YOUR_PLAYLIST_ID")
your_tracks = get_all_tracks(your_pl_id)

our_pl_id = os.getenv("OUR_PLAYLIST_ID")
our_tracks = get_all_tracks(our_pl_id)

new_tracks = my_tracks.union(your_tracks) - our_tracks
pprint(new_tracks)

def add_to_playlist(playlist, tracks):
    """Add to playlist the tracks in chunk of 100 tracks 
    as the API only supports a maximum of 100 tracks per
    request.
    """

    chunks = [tracks[x:x+100] for x in range(0, len(tracks), 100)]
    for chunk in chunks:
        sp.playlist_add_items(playlist, chunk)
add_to_playlist(our_pl_id, list(new_tracks))
