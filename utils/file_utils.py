import csv
import random


def read_file(filename: str) -> list:
        """
    Read a CSV file and return a list of names.

    Args:
        filename (str): The path to the CSV file to be read.

    Returns:
        list: A list containing names read from the CSV file.
    """
    with open(filename, newline='') as new_colleges_file:
        csvreader = csv.reader(new_colleges_file)
        return [name[0] for name in csvreader]


def random_assign(names: list) -> list:
    """
    Randomly shuffle a list of names.

    Args:
        names (list): A list of names to be shuffled.

    Returns:
        list: A new list containing the names shuffled randomly.

    Note:
        This function modifies the input list in place and returns a reference to it.
        To preserve the original list, make a copy of it before calling this function.

    Examples:
        >>> names = ['Alice', 'Bob', 'Charlie', 'David']
        >>> random_assign(names)
        ['Charlie', 'David', 'Alice', 'Bob']
    """
    random.shuffle(names)
    return names
