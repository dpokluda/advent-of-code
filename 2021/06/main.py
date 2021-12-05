def split(line):
    return [int(c) for c in line[:-1]]


def get_bits_counts(lines_bits):
    bits_length = len(lines_bits[0])
    bits_count = []
    for index in range(0, bits_length):
        bits_count += [0]
    for line_bits in lines_bits:
        if len(line_bits) < bits_length:
            print(line_bits)
        for index in range(0, bits_length):
            if line_bits[index] == 1:
                bits_count[index] += 1
    return bits_count


def convert_from_binary(bits):
    result = 0
    for index in range(0, len(bits)):
        bit = bits[index]
        result += bit * 2 ** (len(bits) - index - 1)
    return result


def filter_lines_bits(lines_bits, value, bit_index):
    result = []
    for line_bits in lines_bits:
        if line_bits[bit_index] == value:
            result.append(list(line_bits))
    return result


def get_number(lines_bits, is_major, from_bit_index=0):
    number_of_lines = len(lines_bits)
    bits_count = get_bits_counts(lines_bits)
    # print(from_bit_index)
    # print(bits_count)
    if is_major:
        if bits_count[from_bit_index] > number_of_lines // 2 or bits_count[from_bit_index] == number_of_lines // 2 and number_of_lines % 2 == 0:
            filtered = filter_lines_bits(lines_bits, 1, from_bit_index)
        else:
            filtered = filter_lines_bits(lines_bits, 0, from_bit_index)
    else:
        if bits_count[from_bit_index] > number_of_lines // 2 or bits_count[from_bit_index] == number_of_lines // 2 and number_of_lines % 2 == 0:
            filtered = filter_lines_bits(lines_bits, 0, from_bit_index)
        else:
            filtered = filter_lines_bits(lines_bits, 1, from_bit_index)
    if len(filtered) == 1:
        return filtered
    return get_number(filtered, is_major, from_bit_index+1)


def run():
    file = open('input.txt', 'r')
    lines = file.readlines()
    lines_bits = []
    for line in lines:
        lines_bits.append(list(split(line)))

    oxygen_generator_rating_bits = get_number(lines_bits, True)[0]
    # print(oxygen_generator_rating_bits)
    oxygen_generator_rating = convert_from_binary(oxygen_generator_rating_bits)
    # print(oxygen_generator_rating)
    co2_scrubber_rating_bits = get_number(lines_bits, False)[0]
    # print(co2_scrubber_rating_bits)
    co2_scrubber_rating = convert_from_binary(co2_scrubber_rating_bits)
    # print(co2_scrubber_rating)
    print(oxygen_generator_rating * co2_scrubber_rating)


if __name__ == '__main__':
    run()
