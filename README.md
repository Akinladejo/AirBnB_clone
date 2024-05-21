#AirBnB Clone - The Console
---------------------------
Description
----------------
This project is a fundamental step in the Alx Software Engineer program, aiming to create a comprehensive AirBnB clone. The initial phase involves developing a custom command-line interface (CLI) for data management and establishing essential base classes for data storage.

Usage
---------
The console operates both in interactive and non-interactive modes, similar to a Unix shell. Users are prompted with the (hbnb) command line, where they can enter various commands to interact with the application.

Commands
---------
Run the console: ./console.py
Quit the console: (hbnb) quit
Display help for a command: (hbnb) help <command>
Create an object: (hbnb) create <class>
Show an object: (hbnb) show <class> <id> or (hbnb) <class>.show(<id>)
Destroy an object: (hbnb) destroy <class> <id> or (hbnb) <class>.destroy(<id>)
Show all objects: (hbnb) all or (hbnb) all <class>
Update an attribute of an object: (hbnb) update <class> <id> <attribute_name> "<attribute_value>" or (hbnb) <class>.update(<id>, <attribute_name>, "<attribute_value>")
Models
The models folder contains essential classes for the project:

BaseModel: Base class for all other classes, including id, created_at, and updated_at.
User: Class for storing user information, with attributes email, password, first_name, and last_name.
Amenity: Class for amenity information, featuring the name attribute.
City: Class for location information, storing state_id and name.
State: Class for location information, featuring the name attribute.
Place: Class for accommodation information, with attributes such as city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, and amenity_ids.
Review: Class for user/host review information, storing place_id, user_id, and text.
File Storage
The engine folder manages serialization and deserialization of data in JSON format:

FileStorage: Class for handling data flow, including methods for conversion to/from dictionaries and JSON strings.
Tests
All code is rigorously tested using the unittest module. Test files for classes are located in the test_models folder.

Authors
Osei Kofi: Alx student with a background in mathematics and a passion for programming. LinkedIn | Twitter
