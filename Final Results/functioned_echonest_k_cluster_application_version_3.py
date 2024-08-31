# Import necessary libraries
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib  # Import joblib for loading the model
# from google.colab import drive

# Load the trained KMeans model
kmeans = joblib.load("/content/drive/Shareddrives/Machine Learning Group Project/Final Google Colabs/final_k_cluster_model_with_250_clusters")

trained_csv = pd.read_csv("/content/drive/Shareddrives/Machine Learning Group Project/Final Google Colabs/echonest_clusters_final_version_250_clusters.csv")

# tracks = pd.read_csv("/content/drive/Shareddrives/Machine Learning Group Project/Final Google Colabs/Copy of raw_tracks.csv")

def k_cluster_main(df):
  if "liveness" in df:
    df = df.drop("liveness", axis = 1)
  if "Liveness" in df:
    df = df.drop("liveness", axis = 1)

  new_features = df.values
  scaler = StandardScaler()
  scaler.fit(new_features)
  new_features_scaled = scaler.transform(new_features)
  df['Cluster'] = kmeans.predict(new_features_scaled)
  new_data_cluster = df.iloc[0]['Cluster'] # holds the cluster that the new data falls under
  filtered_df = trained_csv[trained_csv['Cluster'] == new_data_cluster]
  values_list = filtered_df['track_id'].dropna().tolist()
  selected_columns = ['track_id', 'artist_name', 'track_title']


  tracks = pd.read_csv("/content/drive/Shareddrives/Machine Learning Group Project/Final Google Colabs/Copy of raw_tracks.csv")
  tracks = tracks[selected_columns]
  tracks_filtered = tracks[tracks['track_id'].isin(values_list)]

  return tracks_filtered