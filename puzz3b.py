from shared import read_input


BIT_LENGTH = 12


class NoTerminationError(Exception):
    pass


def get_life_support_rating():
    data_with_newlines = read_input('input3.txt', cast_type=str)
    data = [d.strip() for d in data_with_newlines]
    
    oxygen_rating = get_oxygen_rating(data)
    co2_rating = get_co2_rating(data)
    return oxygen_rating * co2_rating


def parse_data(bin_str, ctr):
    new_counter = []
    for ix, bit in enumerate(bin_str):
        if bit == '0':
            new_value = (ctr[ix][0] + 1, ctr[ix][1])
        elif bit == '1':
            new_value = (ctr[ix][0], ctr[ix][1] + 1)
        new_counter.append(new_value)
    return new_counter


def get_rating(data, value_of_more_common_bit):
    for pos in range(BIT_LENGTH):
        counter = [(0, 0)] * BIT_LENGTH
        for bit_str in data:
            counter = parse_data(bit_str, counter)
        if counter[pos][1] >= counter[pos][0]:
            bit_to_keep = str(int(value_of_more_common_bit))
        else:
            bit_to_keep = str(int(not value_of_more_common_bit))
        data = filter_data(data, pos, bit_to_keep)
        
        if len(data) == 1:
            return int(data[0], base=2)
    raise NoTerminationError()


def get_oxygen_rating(data):
    return get_rating(data, value_of_more_common_bit=1)


def get_co2_rating(data):
    return get_rating(data, value_of_more_common_bit=0)


def filter_data(data, pos, bit_val_to_keep):
    valid_bit_strs = []
    for bit_str in data:
        if bit_str[pos] == bit_val_to_keep:
            valid_bit_strs.append(bit_str)
    return valid_bit_strs
    

_runner = get_life_support_rating
