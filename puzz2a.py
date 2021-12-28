from shared import read_input


def change_position(direction, coordinate):
    incr = int(direction.split(' ')[1])
    if 'forward' in direction:
        coordinate = (coordinate[0] + incr, coordinate[1])
    elif 'down' in direction:
        coordinate = (coordinate[0], coordinate[1] + incr)
    elif 'up':
        coordinate = (coordinate[0], coordinate[1] - incr)
    return coordinate


def calculate_destination():
    data = read_input('input2.txt', cast_type=str)
    coordinate = (0, 0)
    for step in data:
        coordinate = change_position(step, coordinate)
    destination = coordinate[0] * coordinate[1]
    return destination


_runner = calculate_destination
