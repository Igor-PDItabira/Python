import pandas as pd

file_path = 'spotify-2023.csv'

df = pd.read_csv(file_path, encoding='latin-1')

df_filtered = df[(df['released_year'] >= 2012) & (df['released_year'] <= 2022)]

df_filtered = df_filtered[~df_filtered['track_name'].str.contains('"')]
df_filtered = df_filtered[~df_filtered['artist(s)_name'].str.contains('"')]

top_tracks = []

for year in range(2012, 2023):
    year_data = df_filtered[df_filtered['released_year'] == year]

    top_track = year_data.loc[year_data['streams'].idxmax()]

    top_tracks.append([
        top_track['track_name'],
        top_track['artist(s)_name'],
        top_track['released_year'],
        top_track['streams']
    ])

print(top_tracks)
