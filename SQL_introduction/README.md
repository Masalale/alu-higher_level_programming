# SQL Introduction

This repository contains a collection of SQL scripts for the MySQL database management system.

## Description

This project introduces fundamental SQL operations.

- `0-list_databases.sql`: Lists all databases on the MySQL server
- `1-create_database_if_missing.sql`: Creates the hbtn_0c_0 database if it doesn't exist
- `2-remove_database.sql`: Deletes the hbtn_0c_0 database if it exists
- `3-list_tables.sql`: Lists all tables in a specified database
- `4-first_table.sql`: Creates a table called first_table with id and name columns
- `5-full_table.sql`: Displays the full description/structure of the first_table
- `6-list_values.sql`: Lists all rows in the first_table
- `7-insert_value.sql`: Inserts a new row with id=89 and name='Best School' into first_table
- `8-count_89.sql`: Counts the number of records with id=89 in first_table
- `9-full_creation.sql`: Creates second_table with multiple rows of data
- `10-top_score.sql`: Lists all records of second_table ordered by score (highest first)
- `11-best_score.sql`: Lists records with score >= 10 in second_table
- `12-no_cheating.sql`: Updates Bob's score to 10 in second_table
- `13-change_class.sql`: Removes all records with score <= 5 in second_table
- `14-average.sql`: Computes the average score of all records in second_table
- `15-groups.sql`: Lists the number of records with the same score in second_table
- `16-no_link.sql`: Lists all records with a name value in second_table ordered by score