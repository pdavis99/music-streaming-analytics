import pandas as pd 
from sqlalchemy import create_engine 

#Connect to database
engine = create_engine("postgresql://postgres:postgres@localhost:5432/music_analytics")

#Load CSV into pandas 
df = pd.read_csv(r"C:\Users\Patrice Davis\Desktop\Projects\Music_Streaming_Analytics\data\sample_dataset.csv")

#Creates a table called 'tracks' if it doesn’t already exist, and loads the dataset into it
df.to_sql("tracks", engine, if_exists="replace", index=False)