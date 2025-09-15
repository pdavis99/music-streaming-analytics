import pandas as pd
from sqlalchemy import create_engine 

engine = create_engine("postgresql://postgres:postgres@localhost:5432/music_analytics")

#Reading whats on the table named "tracks" 
df = pd.read_sql("SELECT * FROM tracks;", engine)

# Standardize blanks to NaN
df['artists'] = df['artists'].replace('', pd.NA)
df['album_name'] = df['album_name'].replace('', pd.NA)
df['track_name'] = df['track_name'].replace('', pd.NA)

#Fill missing values
df['artists'] = df['artists'].fillna("Unknown Artist")
df['album_name'] = df['album_name'].fillna("Unknown Album")
df['track_name'] = df['track_name'].fillna("Untitled Track")

# Fill string columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip().replace('', pd.NA).fillna("Unknown")

# Fill numeric columns
for col in df.select_dtypes(include='number').columns:
    df[col] = df[col].fillna(df[col].median())






#Save back to database
df.to_sql("tracks_cleaned", engine, if_exists="replace", index=False)

