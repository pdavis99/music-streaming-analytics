import pandas as pd 
from sqlalchemy import create_engine 
import seaborn as sns
import matplotlib.pyplot as plt

#Connect to database
engine = create_engine(r"postgresql://postgres:postgres@localhost:5432/music_analytics")

#Load CSV into pandas 
df = pd.read_csv(r"C:\Users\Patrice Davis\Desktop\Projects\Music_Streaming_Analytics\data\sample_dataset.csv") 

# Correlation with popularity
# Select only numeric columns for correlation
numeric_cols = ['danceability', 'energy', 'valence', 'acousticness', 
                'instrumentalness', 'tempo', 'popularity']

correlations = df[numeric_cols].corr()['popularity'].sort_values(ascending=False)
print("Correlation with popularity:\n", correlations)

# Generate scatter plots to visualize the relationship between each audio feature
# and track popularity. This helps identify trends or patterns, even if correlations
# are weak. Alpha is set to 0.5 to reduce overlap for dense areas.
features = ['danceability', 'energy', 'valence', 'acousticness', 'instrumentalness', 'tempo']

# Create subplots
fig, axes = plt.subplots(2, 3, figsize=(18,10))
axes = axes.flatten()

for i, feature in enumerate(features):
    sns.scatterplot(x=df[feature], y=df['popularity'], alpha=0.5, ax=axes[i])
    axes[i].set_title(f'{feature.capitalize()} vs Popularity')
    axes[i].set_xlabel(feature.capitalize())
    axes[i].set_ylabel('Popularity')

plt.tight_layout(pad=3.0)  # increases spacing between subplots so titles/labels don't overlap
plt.show()
  

# Select audio features + popularity
features = ['danceability', 'energy', 'valence', 'acousticness', 'instrumentalness', 'tempo', 'popularity']
df_features = df[features]

# Create correlation matrix
corr_matrix = df_features.corr()

# Plot heatmap
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap: Audio Features vs Popularity')
plt.show()