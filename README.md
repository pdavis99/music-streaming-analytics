# 🎶 Spotify Music Analysis



## 📌 Project Overview

This project explores what makes a song popular using a Spotify dataset.  

The dataset was cleaned and analyzed using both **Python (Pandas + SQLAlchemy)** and **PostgreSQL (SQL queries)**.  



---

## ⚙️ Tools \& Technologies

\- **Python** (data cleaning and visualization: Pandas, SQLAlchemy, Seaborn, Matplotlib)  

\- **PostgreSQL** (data storage \& querying)  

\- **SQL** (data cleaning and analysis)  



---



## 📊 Data Cleaning \& Preparation



### 🔹 Dataset Overview

\- **Total tracks (raw):** 81,201  

\- **Key columns:** `track\_id`, `track\_name`, `artists`, `album\_name`, `duration\_ms`, `popularity`, `danceability`, `energy`, `valence`, `track\_genre`  

\- **Source:** Spotify sample dataset (CSV file provided).  



### 🔹 Cleaning in SQL

1\. **Removed duplicate rows**  

&nbsp;  - Deduplicated on (`track\_name`, `artists`) combination.  

2\. **Standardized text columns**  

&nbsp;  - Applied `TRIM()` to remove leading/trailing spaces.  

3\. **Handled invalid durations**  

&nbsp;  - Removed tracks with `duration\_ms = 0`.  

&nbsp;  - Removed tracks with `duration\_ms > 900,000 ms` (~15 minutes).  



### 🔹 SQL Scripts

All SQL queries used for data cleaning, deduplication, and summarization are stored in the `sql/` folder.  

These scripts can be run to reproduce the cleaned dataset (`tracks\_cleaned`) used for analysis.



### 🔹 Cleaning in Python

1\. **Loaded dataset into PostgreSQL** using SQLAlchemy.  

2\. **Standardized missing values**:  

&nbsp;  - Replaced blanks (`''`) with `NaN`.  

&nbsp;  - Filled missing `artists`, `album\_name`, and `track\_name` with `"Unknown Artist"`, `"Unknown Album"`, `"Untitled Track"`.  

3\. **Trimmed whitespace** in string columns.  

4\. **Replaced empty strings with `"Unknown"`** across all text fields.  

5\. **Filled numeric columns** with their median values.  

6\. **Saved cleaned data** back into PostgreSQL as `tracks\_cleaned`.  



### 🔹 Summary Statistics (after cleaning)

| Metric              | Value   |

|----------------------|---------|

| **Total tracks**     | 81,201  |

| **Avg popularity**   | 34.7    |

| **Popularity stdev** | 19.3    |

| **Avg danceability** | 0.56    |

| **Avg energy**       | 0.64    |

| **Avg valence**      | 0.46    |



\- **Popularity range:** 0 – 100 (valid, no errors found).  

\- **Duration distribution:** Most songs are ~3–4 minutes, consistent with typical music.  



👉 The final cleaned dataset is stored as a new table: `**tracks\_cleaned**`.  



---



## 🔍 Popularity Analysis

**Question:** What makes a song popular?  



We analyzed audio features such as danceability, energy, valence, acousticness, instrumentalness, and tempo to see how they relate to popularity.  



Correlation analysis was performed in Python (pandas).  



### 🔹 Correlation with Popularity



| Feature          | Correlation with Popularity | Interpretation |

|------------------|-----------------------------|----------------|

| Danceability     | 0.035                       | Slight positive effect |

| Tempo            | 0.013                       | Almost no effect |

| Energy           | 0.001                       | No meaningful relationship |

| Acousticness     | -0.025                      | Slight negative effect |

| Valence          | -0.041                      | Very weak negative effect |

| Instrumentalness | -0.095                      | Instrumental tracks tend to be less popular |



---



## 📌 Key Takeaways

\- Instrumental content is the strongest (though still small) predictor of **lower popularity**.  

\- Danceable songs have a **tiny positive influence** on popularity.  

\- Overall, **audio features alone explain very little** of popularity; other factors like artist reputation, marketing, or cultural trends likely play a larger role.  



---



## 📊 Visualizations

Scatter plots and heatmaps were generated to explore these relationships visually.  

🔹 All plots are saved in the `visualizations/` folder and displayed below.  



### 🔹 Correlation Heatmap

!\[Heatmap of audio features vs popularity](visualizations/Audio Features vs Popularity Heatmaps.png)



### 🔹 Danceability vs Popularity

!\[Scatter plot of danceability vs popularity](visualizations/Audio Features vs Popularity Scatter Plots.png)



---



## 📝 Findings \& Summary 

\- **Scatter Plots:** The scatter plots showed a random distribution of points. For every audio feature, songs with low, medium, and high popularity scores were present across the entire range of the feature's values. There was no visible upward or downward trend.  

\- **Correlation Heatmap:** The heatmap confirmed the visual findings. Correlation coefficients between all audio features and popularity were very close to zero, ranging from **-0.10 to 0.04**.  



👉 For example, the correlation between *danceability* and *popularity* was only **0.04**, suggesting that a song's danceability score is not a reliable predictor of its popularity.  



---



## 📂 Repository Structure



