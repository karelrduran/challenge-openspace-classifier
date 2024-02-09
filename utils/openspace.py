from .table import Table
from utils.file_utils import read_file, random_assign


class Openspace:
    """
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
    """
    def __init__(self):
        self.number_of_tables: int = 6
        self._tables: list = []
        for i in range(self.number_of_tables):
            self._tables.append(Table())

    def organize(self, names: list):
        """
        Randomly assign people to Seat objects in the different Table objects
        :param names:
        :return:
        """
        random_list = random_assign(names=names)
        for table in self._tables:
            for i in range(table.capacity):
                if random_list:
                    table.assign_seat(random_list.pop())

    def display(self):
        """
        Display the different tables and there occupants
        :return:
        """
        for table in self._tables:
            print(table)
            for seat in table.seats:
                print(seat)

    def store(self, filename: str):
        """
        Store the repartition in an Excel file
        :param filename:
        :return:
        """
        with open(file=filename, mode='w') as output_file:
            for table in self._tables:
                for seat in table.seats:
                    output_file.write(seat.occupant + '\n')

    def __str__(self):
        """

        :return:
        """
        return f"This is an openspace with {self.number_of_tables} tables"
