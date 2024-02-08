import csv
import random


def read_file(filename: str) -> list:
    with open(filename, newline='') as new_colleges_file:
        csvreader = csv.reader(new_colleges_file)
        return [name[0] for name in csvreader]


def random_assign(names: list) -> list:
    random.shuffle(names)
    return names
