# Python Object-Relational Mapping

## Description
This project connects databases and Python using both MySQLdb (a MySQL database connector) and SQLAlchemy (an Object Relational Mapper). The project demonstrates how to write SQL queries within Python code and how to use ORM to abstract database operations into Python objects.


### MySQL Connection Scripts (Direct SQL)
- **0-select_states.py**: Lists all states from the database hbtn_0e_0_usa
- **1-filter_states.py**: Lists all states with a name starting with 'N'
- **2-my_filter_states.py**: Takes a state name as argument and displays matching states
- **3-my_safe_filter_states.py**: Same as the previous script but protected from SQL injection
- **4-cities_by_state.py**: Lists all cities from the database with their state names
- **5-filter_cities.py**: Lists all cities of a given state

### SQLAlchemy ORM Implementation
- **model_state.py**: Contains the State class definition mapping to the states table
- **7-model_state_fetch_all.py**: Lists all State objects from the database
- **8-model_state_fetch_first.py**: Prints the first State object from the database
- **9-model_state_filter_a.py**: Lists all State objects containing the letter 'a'
- **10-model_state_my_get.py**: Prints the State object with a specified name
- **11-model_state_insert.py**: Adds a new State object to the database
- **12-model_state_update_id_2.py**: Changes the name of a State object with id=2
- **13-model_state_delete_a.py**: Deletes all State objects with a name containing 'a'
- **model_city.py**: Contains the City class definition mapping to the cities table
- **14-model_city_fetch_by_state.py**: Prints all City objects from the database
