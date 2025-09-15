-- 🔹 Remove duplicate rows by keeping only one record 
--    per (track_name, artists) combination
DELETE FROM tracks a
USING tracks b
WHERE a.track_id < b.track_id
  AND a.track_name = b.track_name
  AND a.artists = b.artists;

-- 🔹 Check if there are still duplicate tracks left 
--    (same track_name + artists with more than 1 record)
SELECT track_name, artists, COUNT(*)
FROM tracks
GROUP BY track_name, artists
HAVING COUNT(*) > 1;

-- 🔹 Remove leading/trailing spaces from text columns 
--    (standardizes the text data)
UPDATE tracks
SET track_name = TRIM(track_name),
    album_name = TRIM(album_name),
    artists = TRIM(artists),
    track_genre = TRIM(track_genre);

--checking if any rows have null values
SELECT 
  SUM(CASE WHEN popularity IS NULL THEN 1 ELSE 0 END) AS null_popularity,
  SUM(CASE WHEN danceability IS NULL THEN 1 ELSE 0 END) AS null_danceability,
  SUM(CASE WHEN energy IS NULL THEN 1 ELSE 0 END) AS null_energy,
  SUM(CASE WHEN valence IS NULL THEN 1 ELSE 0 END) AS null_valence,
  SUM(CASE WHEN duration_ms IS NULL THEN 1 ELSE 0 END) AS null_duration
FROM tracks;

--check duration outliers(e.g., > 15 minutes = 900,000 ms)
SELECT 
    MIN(duration_ms) AS min_duration,
    MAX(duration_ms) AS max_duration,
    AVG(duration_ms) AS avg_duration,
    PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY duration_ms) AS p99_duration
FROM tracks;

--deleting outliers from table. 
DELETE FROM tracks
WHERE duration_ms = 0
   OR duration_ms > 900000;

--checking to see if there's any outliers in the popularity column
SELECT 
    MIN(popularity) AS min_popularity,
    MAX(popularity) AS max_popularity,
    AVG(popularity) AS avg_popularity
FROM tracks;

-- Create a cleaned view with only valid tracks
CREATE OR REPLACE VIEW tracks_valid AS
SELECT *
FROM tracks
WHERE duration_ms > 0                
  AND duration_ms <= 900000           
  AND popularity BETWEEN 0 AND 100     
  AND danceability IS NOT NULL         
  AND energy IS NOT NULL
  AND valence IS NOT NULL;

-- Check average popularity and audio features across all valid tracks
SELECT
  COUNT(*) AS total_tracks,
  AVG(popularity) AS avg_popularity,
  STDDEV_POP(popularity) AS pop_stddev,
  AVG(danceability) AS avg_danceability,
  AVG(energy) AS avg_energy,
  AVG(valence) AS avg_valence
FROM tracks_valid;
