CREATE TABLE tracks (
    track_id VARCHAR(50) PRIMARY KEY,
    artists VARCHAR(50) NULL,    
    album_name VARCHAR(50) NULL,
    track_name VARCHAR(50) NULL,
    popularity INT NULL,
    duration_ms INT NULL,
    explicit BOOLEAN NULL,
    danceability DECIMAL NULL,
    energy DECIMAL NULL,
    key INT NULL.
    loudness DECIMAL NULL,
    mode INT NULL,
    speechiness DECIMAL NULL,
    acousticness DECIMAL NULL,
    instrumentalness DOUBLE PRECISION NULL,
    liveness DECIMAL NULL,
    valence DECIMAL NULL,
    tempo DECIMAL NULL,
    time_signature INT NULL,
    track_genre VARCHAR(50) NULL
);
