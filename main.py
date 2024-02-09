import argparse
import os

from utils.file_utils import read_file, random_assign
from utils.openspace import Openspace


def run(argv=None, save_main_session=True):
    """
    Run the program to organize new colleagues in an openspace.

    Args:
        argv: List of command-line arguments. If None, command-line arguments will be taken from sys.argv.
        save_main_session: Whether to save the main session state. Default is True.

    Description:
        This function parses command-line arguments to specify input and output file paths.
        It then reads the data from the input file, organizes it using the Openspace class,
        displays the organized data, and stores it in the specified output file.

    Usage:
        To run the program with default input and output file paths:
            run()

        To specify custom input and output file paths:
            run(['--input', 'path/to/input/file.csv', '--output', 'path/to/output/file.csv'])

        Tu run the program in the terminal:
            python script.py [--input 'path/to/input/file.csv'] [--output 'path/to/output/file.csv']

    """
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
