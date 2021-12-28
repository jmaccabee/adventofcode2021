from shared import read_input

from collections import namedtuple


Coordinate = namedtuple('Coordinate', 'position depth aim')

def change_position(direction, coord):
    incr = int(direction.split(' ')[1])
    if 'forward' in direction:
        coord = Coordinate(
            coord.position + incr, coord.depth + (coord.aim * incr), coord.aim
        )
    elif 'down' in direction:
        coord = Coordinate(
            coord.position, coord.depth, coord.aim + incr
        )
    elif 'up':
        coord = Coordinate(
            coord.position, coord.depth, coord.aim - incr
        )
    return coord


def calculate_destination():
    data = read_input('input2.txt', cast_type=str)
    coord = Coordinate(0, 0, 0)
    for step in data:
        coord = change_position(step, coord)
    destination = coord.position * coord.depth
    return destination


_runner = calculate_destination
