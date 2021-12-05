def split(line):
    return [int(c) for c in line[:-1]]


def get_rate(bits, total, is_major):
    result = 0
    for index in range(0, len(bits)):
        bit = bits[index]
        if bit > total // 2:
            if is_major is True:
                number = 1
            else:
                number = 0
        else:
            if is_major is True:
                number = 0
            else:
                number = 1
        result += number*2**(len(bits)-index-1)
    return result
            

def run():
    file = open('test.txt', 'r')
    lines = file.readlines()
    lines_bits = []
    for line in lines:
        lines_bits.append(list(split(line)))
    number_of_lines = len(lines_bits)
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

    # print(bits_count)
    gamma_rate = get_rate(bits_count, number_of_lines, True)
    epsilon_rate = get_rate(bits_count, number_of_lines, False)
    # print(gamma_rate)
    # print(epsilon_rate)
    print(gamma_rate * epsilon_rate)


if __name__ == '__main__':
    run()
