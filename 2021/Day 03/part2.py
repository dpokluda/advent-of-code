def calculate_rating(lines_bits, is_normal_mode):
    filtered = lines_bits
    index = -1
    filter_major_value = 1 if is_normal_mode else 0
    filter_minor_value = 0 if is_normal_mode else 1

    while len(filtered) > 1:
        index += 1
        if [line[index] for line in filtered].count(1) * 2 >= len(filtered):
            filtered = list(filter(lambda x: x[index] == filter_major_value, filtered))
        else:
            filtered = list(filter(lambda x: x[index] == filter_minor_value, filtered))
    return filtered


def convert_from_binary(bits):
    length = len(bits)
    result = 0
    for index in range(0, length):
        result += bits[index] * 2 ** (length - index - 1)
    return result


def run():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    lines_bits = []
    for line in lines:
        lines_bits.append([int(c) for c in line])

    filtered = calculate_rating(lines_bits, True)
    oxygen_generator_rating = convert_from_binary(filtered[0])
    print(oxygen_generator_rating)

    filtered = calculate_rating(lines_bits, False)
    co2_scrubber_rating = convert_from_binary(filtered[0])
    print(co2_scrubber_rating)

    print(oxygen_generator_rating * co2_scrubber_rating)
