# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id SERIAL PRIMARY KEY,
        start_time TIMESTAMP REFERENCES time (start_time),
        user_id INT REFERENCES users (user_id),
        level VARCHAR,
        song_id VARCHAR REFERENCES songs (song_id),
        artist_id VARCHAR REFERENCES artists (artist_id),
        session_id INT NOT NULL,
        location TEXT NOT NULL,
        user_agent TEXT NOT NULL
)
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT PRIMARY KEY,
        first_name VARCHAR,
        last_name VARCHAR,
        gender TEXT,
        level VARCHAR
)
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR PRIMARY KEY,
        title VARCHAR NOT NULL,
        artist_id VARCHAR REFERENCES artists (artist_id),
        year INT NOT NULL,
        duration FLOAT NOT NULL
)
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR PRIMARY KEY,
        name VARCHAR NOT NULL,
        location TEXT,
        latitude FLOAT,
        longitude FLOAT
)
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time TIMESTAMP PRIMARY KEY,
        hour INT NOT NULL,
        day INT NOT NULL,
        week INT NOT NULL,
        month INT NOT NULL,
        year INT NOT NULL,
        weekday VARCHAR NOT NULL
        
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [time_table_create, user_table_create, artist_table_create, song_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]