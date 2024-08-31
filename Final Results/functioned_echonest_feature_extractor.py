# install urllib3

import urllib.parse
import spotipy

def spotify_setup():
  # Define URI
  uri_string = "https://example.com/path?param1=value1&param2=value2"

  # Parse the URI
  parsed_uri = urllib.parse.urlparse(uri_string)

  # Access components
  scheme = parsed_uri.scheme
  netloc = parsed_uri.netloc
  path = parsed_uri.path
  query = parsed_uri.query

  print("Scheme:", scheme)
  print("Netloc:", netloc)
  print("Path:", path)
  print("Query:", query)

# spotify_setup()

# # Define URI
# uri_string = "https://example.com/path?param1=value1&param2=value2"

# # Parse the URI
# parsed_uri = urllib.parse.urlparse(uri_string)

# # Access components
# scheme = parsed_uri.scheme
# netloc = parsed_uri.netloc
# path = parsed_uri.path
# query = parsed_uri.query

# print("Scheme:", scheme)
# print("Netloc:", netloc)
# print("Path:", path)
# print("Query:", query)

"""### Actual Spotify stuff"""

# pip install spotipy

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re
import pandas as pd

client_id = 'e958b5cfde674a8d8e07f1bb3cba2322'
client_secret = 'd79ebf15dbc6446084f11794f2bb32ea'
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def song_feature_extraction(url):
    # Extract track ID from the URL
    match = re.search(r'track/(\w+)', url)
    if not match:
        print("Invalid Spotify URL")
        return None

    track_id = match.group(1)

    # Check if track_id is valid
    if not track_id:
        print("Failed to extract track ID.")
        return None

    # Construct Spotify URI
    track_uri = f'spotify:track:{track_id}'

    # Retrieve track features
    track_features = sp.audio_features(track_uri)

    # Check if track features are available
    if not track_features:
        print("Track features not available.")
        return None

    # Extract relevant features
    features = track_features[0]

    # Define the desired order of columns
    column_order = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'tempo', 'valence']

    # Filter and reorder the features
    selected_features = {col: features[col] for col in column_order}

    # Convert the selected features to a DataFrame
    df = pd.DataFrame([selected_features])

    # You can return the DataFrame or process it further if needed
    return df

# df = song_feature_extraction("https://open.spotify.com/track/3CRDbSIZ4r5MsZ0YwxuEkn?si=c8501be08ef4437e")

# df.head()






# #@title Function to extract track features and return a DataFrame
# def extract_track_features(track_id):
#     # Check if track_id is valid
#     if not track_id:
#         print("Failed to extract track ID.")
#         return None

#     # Construct Spotify URI
#     track_uri = f'spotify:track:{track_id}'

#     # Retrieve track features
#     track_features = sp.audio_features(track_uri)

#     # Check if track features are available
#     if not track_features:
#         print("Track features not available.")
#         return None

#     # Extract relevant features
#     features = track_features[0]

#     # Display track features
#     # print("Track Features:")
#     # print("Acousticness:", features['acousticness'])
#     # print("Danceability:", features['danceability'])
#     # print("Energy:", features['energy'])
#     # print("Instrumentalness:", features['instrumentalness'])
#     # print("Liveness:", features['liveness'])
#     # print("Speechiness:", features['speechiness'])
#     # print("Tempo:", features['tempo'])
#     # print("Valence:", features['valence'])

#     # Creating DataFrame and adding track features to it
#     columns = ['Acousticness', 'Danceability', 'Energy', 'Instrumentalness', 'Liveness', 'Speechiness', 'Tempo', 'Valence']
#     df = pd.DataFrame(columns=columns)

#     # Append the features to the DataFrame
#     feature_values = [features['acousticness'], features['danceability'], features['energy'],
#                       features['instrumentalness'], features['liveness'], features['speechiness'],
#                       features['tempo'], features['valence']]

#     df = df.append(pd.Series(feature_values, index=columns), ignore_index=True)

#     # Display the DataFrame if needed
#     print("DataFrame after adding track features:")
#     # print(df)

#     return df
