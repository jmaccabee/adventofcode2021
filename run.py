import shared

import sys


if __name__ == '__main__':
    pymodule = sys.argv[1].split('.py')[0]
    shared._run_module(pymodule)
