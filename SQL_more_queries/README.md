# SQL More Queries

This repository contains advanced SQL query scripts for MySQL database management system.
## Description

This project explores more complex SQL operations.

- `0-privileges.sql`: Lists all privileges of MySQL users user_0d_1 and user_0d_2
- `1-create_user.sql`: Creates the MySQL server user user_0d_1 with all privileges
- `2-create_read_user.sql`: Creates the database hbtn_0d_2 and user user_0d_2 with SELECT privilege
- `3-force_name.sql`: Creates a table force_name with a NOT NULL constraint
- `4-never_empty.sql`: Creates a table with an id column that cannot be empty
- `5-unique_id.sql`: Creates a table with a column that must have unique values
- `6-states.sql`: Creates a database and table with a PRIMARY KEY
- `7-cities.sql`: Creates a cities table with a FOREIGN KEY referencing the states table
- `8-cities_of_california_subquery.sql`: Lists all cities of California using a subquery
- `9-cities_by_state_join.sql`: Lists all cities with their state names using JOIN
- `10-genre_id_by_show.sql`: Lists shows with at least one linked genre
- `11-genre_id_all_shows.sql`: Lists all shows with their genre IDs (or NULL)
- `12-no_genre.sql`: Lists shows that don't have a genre linked
- `13-count_shows_by_genre.sql`: Counts shows by genre
- `14-my_genres.sql`: Lists genres of a specific show
- `15-comedy_only.sql`: Lists all Comedy shows
- `16-shows_by_genre.sql`: Lists all shows and their linked genres