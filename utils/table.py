class Seat:
    """
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
    """

    def __init__(self, name: str = None):
        """
        Initializes a seat object.

        Args:
            name (str, optional): The name of the occupant. If None, the seat is considered free.
        """
        if name is None:
            self._free: bool = True
            self._occupant: str = ''
        else:
            self._free: bool = False
            self._occupant: str = name

    def set_occupant(self, name: str):
        """
        Assigns a seat to a person if it's available.

        Args:
            name (str): The name of the person to assign to the seat.
        """
        self._occupant = name
        self._free = False

    def remove_occupant(self) -> str:
        """
        Remove someone from the seat and return their name.

        Returns:
            str: The name of the removed occupant.
        """
        occupant = ''
        if not self._free:
            occupant = self._occupant
            self._occupant = None
            self._free = True
        return occupant

    def __str__(self):
        """
        Returns a string representation of the seat.

        Returns:
            str: A string indicating whether the seat is free or occupied.
        """
        if self._free:
            return f"This seat is free"
        else:
            return f"{self._occupant} is seated here"

    @property
    def is_free(self):
        return self._free

    @property
    def occupant(self):
        return self._occupant


class Table:
    """
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
    """

    def __init__(self):
        """
        Initializes a Table object.

        This constructor initializes a Table object with a default capacity of 4 seats.

        Attributes:
            _capacity (int): The maximum number of seats the table can accommodate.
            _seats (list): A list containing Seat objects representing the seats at the table.

        Notes:
            This constructor creates Seat objects for the table based on its capacity.
        """
        self._capacity: int = 4
        self._seats = []
        for i in range(self._capacity):
            self.seats.append(Seat())

    @property
    def capacity(self):
        return self._capacity

    @property
    def seats(self):
        return self._seats

    def has_free_spot(self) -> bool:
        """
        Check if the table has any available spots.
        Returns:
            bool: True if the table has available spots, False otherwise.
        """
        free_space = False
        for seat in self.seats:
            if seat.is_free:
                free_space = True
                break

        return free_space

    def assign_seat(self, name: str) -> None:
        """
        Assigns a person to an available seat at the table.

        Args:
            name (str): The name of the person to be assigned to a seat.

        Returns:
            None
        """
        if self.has_free_spot():
            for seat in self.seats:
                if seat.is_free:
                    seat.set_occupant(name=name)
                    break

    def left_capacity(self) -> int:
        """
        Calculates the number of available seats left at the table.

        Returns:
            int: The number of available seats left.
        """
        if not self.has_free_spot():
            return 0
        else:
            count = 0
            for seat in self.seats:
                if seat.is_free:
                    count += 1
            return count

    def __str__(self):
        """
        Returns a string representation of the table.

        Returns:
            str: A string describing the table's capacity and the number of available seats.
        """
        return f"This table have a _capacity of {self._capacity}, with {self.left_capacity()} seats available"
