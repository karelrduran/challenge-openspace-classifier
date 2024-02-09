<h1 align="center"> Open space organizer </h1>

![Openspace](img/openspace.png)

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Mission](#mission)
- [Usage](#usage)
- [Arguments](#arguments)
- [Dependencies](#dependencies)
- [Timeline](#timeline)
- [Project structure](#project-structure)
- [Class Description](#class-description)
- [Personal situation](#personal-situation)


## Mission

Your company moved to a new office at the Gent Zuiderport. Its an openspace with 6 tables of 4 seats. 
As many of you are new colleagues, you come up with the idea of changing seats everyday and get to know each other better by working side by side with your new colleagues.

You will create a program that runs everyday to re-assign everybody to a new seat. 

## Usage
***
    Usage:
        To run the program with default input and output file paths:
            run()

        To specify custom input and output file paths:
            run(['--input', 'path/to/input/file.csv', '--output', 'path/to/output/file.csv'])

        Tu run the program in the terminal:
            python script.py [--input 'path/to/input/file.csv'] [--output 'path/to/output/file.csv']

## Arguments
***

    * --input: Optional argument to pass the address of the file containing the list of colleagues
    * --output: Optional argument to pass the address of the file where you want to save the last peer distribution in openspace 
    
## Dependencies
    Does not depend on any external library

## Timeline
- **February 8, 2024:** 
  >>> Project kickoff<br>
  >>> Solution development<br>
  >>> Code documentation<br>
              
- **February 9, 2024:** 
  >>> Creation of [README.md](README.md) file


## Project structure

[challenge-openspace-classifier](.)
  * [data/](data)
    * [new_colleagues.csv](data/new_colleagues.csv)
  * [img/](img)
  * [output/](output)
  * [utils/](utils)
    * [file_utils.py](utils/file_utils.py)
    * [openspace.py](utils/openspace.py)
    * [table.py](utils/table.py)
  * [main.py](main.py)
  * [README.md](README.md)


## Class Description
[Openspace class](utils/openspace.py)
```
    Represents an openspace workplace with multiple tables.

    This class models an openspace with a predefined number of tables, where people are randomly assigned
    to seats at each table.

    Attributes:
        number_of_tables (int): The total number of tables in the openspace.
        _tables (list): A list containing Table objects representing the tables in the openspace.

    Methods:
        __init__: Initializes an Openspace object.
        organize: Randomly assigns people to seats in the different tables.
        display: Displays the different tables and their occupants.
        store: Stores the seat assignments in an Excel file.
        __str__: Returns a string representation of the openspace.

    Notes:
        This class relies on the Table class to represent individual tables, and the Seat class to represent seats.
```

[Table class](utils/table.py)
```
    Represents a table object.

    This class models a table with a specific capacity and a set of seats.

    Attributes:
        _capacity (int): The maximum number of seats the table can accommodate.
        _seats (list): A list containing Seat objects representing the seats at the table.

    Methods:
        __init__: Initializes a Table object.
        has_free_spot: Checks if the table has any available spots.
        assign_seat: Assigns a person to an available seat at the table.
        left_capacity: Calculates the number of available seats left at the table.
        __str__: Returns a string representation of the table.

    Notes:
        This class relies on the Seat class to represent individual seats at the table.
```

[Seat class](utils/table.py)
```
    Represents a Seat object.  

    This class models a Seat, which can be occupied by a person or left vacant.

    Attributes:
        _free (bool): A flag indicating whether the seat is free or occupied.
        _occupant (str): The name of the occupant if the seat is occupied.

    Methods:
        __init__: Initializes a seat object.
        set_occupant: Assigns a seat to a person if it's available.
        remove_occupant: Removes someone from the seat and returns their name.
        __str__: Returns a string representation of the seat.
        is_free: Returns True if the seat is free, otherwise False.
        occupant: Returns the name of the occupant of the seat.
```

## Personal situation
While doing this project I was part of the ARAI6 group of the <a href="https://becode.org/all-trainings/pedagogical-framework-ai-data-science/">AI Bootcamp</a> training organized by <a href="https://becode.org/">BeCode</a> in Ghent. The main objective of this project is to provide participants with an opportunity to understand the concepts of object-oriented programming (OOP) in Python.
______________________________________
  <img src="https://avatars.githubusercontent.com/u/106887418?s=400&u=82192b481d8f03c3eaad34ca2bd67889fce6a0c2&v=4" width=115><br><sub>Karel Rodríguez Durán</sub>