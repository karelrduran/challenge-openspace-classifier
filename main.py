import argparse
import os

from utils.file_utils import read_file, random_assign
from utils.openspace import Openspace

list_names = read_file('./data/new_colleges.csv')


def run(argv=None, save_main_session=True):
    path = os.path.abspath('')
    default_input = os.path.join(path, 'data/new_colleagues.csv')
    default_output = os.path.join(path, 'output/output.csv')

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        dest='input',
        default=default_input,
        help='New colleges file name')
    parser.add_argument(
        '--output',
        dest='output',
        default=default_output,
        help='New colleges file name')

    args = parser.parse_args()

    openspace = Openspace()
    openspace.organize(read_file(args.input))
    openspace.display()
    openspace.store(args.output)


if __name__ == '__main__':
    # filename = './data/new_colleagues.csv'
    # outputfile = './output/output.csv'
    run()
