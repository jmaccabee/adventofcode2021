from shared import read_input


def count_increases():
    data = read_input('input1.txt')
    increases = 0
    for i in range(len(data)-1):
	    increases += is_increasing(data[i], data[i+1])
    return increases


def is_increasing(first, second):
    if (second > first):
        return 1
    return 0


_runner = count_increases

