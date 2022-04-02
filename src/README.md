
  
# Project: Data Modeling with Postgres

This project models user activity data for a music streaming app called Sparkify to optimize queries for understanding what songs users are listening to by creating a **Postgres relational database** and **ETL pipeline** to build up **Fact and Dimension tables** and insert data into new tables.




## Project Files
`test.ipynb` displays the first few rows of each table to let you check your database.

`create_tables.py` drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.

`etl.ipynb` reads and processes a single file from song_data and log_data and loads the data into your tables. 

`etl.py` reads and processes files from `song_data` and `log_data` and loads them into your tables.

## ETL Pipeline
### etl.py
ETL pipeline builder

1. `process_data`
	* Iterating dataset to apply `process_song_file` and `process_log_file` functions
2. `process_song_file`
	* Process song dataset to insert record into _songs_ and _artists_ dimension table
3. `process_log_file`
	* Process log file to insert record into _time_ and _users_ dimension table and _songplays_ fact table

### create_tables.py
Creating Fact and Dimension table schema

1. `create_database`
2. `drop_tables`
3. `create_tables`

### sql_queries.py
Helper SQL query statements for `etl.py` and `create_tables.py`

1. `*_table_drop`
2. `*_table_create`
3. `*_table_insert`
4. `song_select`


## Database Schema
### Fact table
```
songplays
	- songplay_id 	PRIMARY KEY
	- start_time 
	- user_id
	- level
	- song_id 
	- artist_id
	- session_id
	- location
	- user_agent
```

### Dimension table
```
users
	- user_id 	PRIMARY KEY
	- first_name
	- last_name
	- gender
	- level
songs
	- song_id 	PRIMARY KEY
	- title
	- artist_id
	- year
	- duration
artists
	- artist_id 	PRIMARY KEY
	- name
	- location
	- latitude
	- longitude
time
	- start_time 	PRIMARY KEY
	- hour
	- day
	- week
	- month
	- year
	- weekday
```
## Datasets

Data is currently collected for song and user activities, in two directories:
`data/log_data` and `data/song_data`, using JSON files.

### Song dataset format

```json
{
  "num_songs": 1,
  "artist_id": "ARGSJW91187B9B1D6B",
  "artist_latitude": 35.21962,
  "artist_longitude": -80.01955,
  "artist_location": "North Carolina",
  "artist_name": "JennyAnyKind",
  "song_id": "SOQHXMF12AB0182363",
  "title": "Young Boy Blues",
  "duration": 218.77506,
  "year": 0
}
```

### Log dataset format

```json
{
  "artist": "Survivor",
  "auth": "Logged In",
  "firstName": "Jayden",
  "gender": "M",
  "itemInSession": 0,
  "lastName": "Fox",
  "length": 245.36771,
  "level": "free",
  "location": "New Orleans-Metairie, LA",
  "method": "PUT",
  "page": "NextSong",
  "registration": 1541033612796,
  "sessionId": 100,
  "song": "Eye Of The Tiger",
  "status": 200,
  "ts": 1541110994796,
  "userAgent": "\"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36\"",
  "userId": "101"
}
```

## Running

To run this project in the **Project Workspace** open up the bash terminal. And to run the scripts in the current directory run:

To create your tables:

```sh
python create_tables.py
```

To populate your tables:

```sh
python etl.py
```
