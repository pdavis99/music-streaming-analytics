import pandas as pd 
from sqlalchemy import create_engine 

#Load CSV into pandas 
df = pd.read_csv(r"C:\Users\Patrice Davis\Desktop\Projects\Music_Streaming_Analytics\data\sample_dataset.csv")

# Connect to PostgreSQL
engine = create_engine("postgresql://postgres:postgres@localhost:5432/music_analytics")

df.to_sql("tracks", engine, if_exists="replace", index=False)