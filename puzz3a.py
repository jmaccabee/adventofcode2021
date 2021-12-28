from shared import read_input


BIT_LENGTH = 12


def get_most_common_bit():
    data_with_newlines = read_input('input3.txt', cast_type=str)
    data = [d.strip() for d in data_with_newlines]
    
    # separately, we asserted that each element in data has the same length
    counter = [(0, 0)] * BIT_LENGTH
    for bin_str in data:
        counter = parse_data(bin_str, counter)

    gamma_rate = make_gamma_rate(counter)
    epsilon_rate = make_epsilon_rate(gamma_rate)
    return gamma_rate * epsilon_rate


def parse_data(bin_str, ctr):
    new_counter = []
    for ix, bit in enumerate(bin_str):
        if bit == '0':
            new_value = (ctr[ix][0] + 1, ctr[ix][1])
        elif bit == '1':  
            new_value = (ctr[ix][0], ctr[ix][1] + 1)
        new_counter.append(new_value)
    return new_counter


def make_gamma_rate(counter):
    gamma_rate = ''
    for pos in counter:
        if pos[0] > pos[1]:
            gamma_rate += '0'
        elif pos[1] > pos[0]:
            gamma_rate += '1'
    return int(gamma_rate, base=2)



def make_epsilon_rate(gamma_rate):    
    epsilon_rate = ''
    # ignore the first two characters of the bit string '0b'
    for bit in str(bin(gamma_rate))[2:]:
        # flip the bit at each position in gamma_rate
        epsilon_rate += '0' if bit == '1' else '1'
    return int(epsilon_rate, base=2)


_runner = get_most_common_bit
