hex_convertor = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
                 '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101',
                 'E': '1110', 'F': '1111'}


def convert_from_binary(value):
    bits = [int(x) for x in value]
    number = 0
    for i in range(0, len(bits)):
        number += bits[i] * 2 ** (len(bits) - i - 1)
    return number


def get_packet(line, from_index, versions):
    version = convert_from_binary(line[from_index:from_index+3])
    # print(f'v={version}')
    versions.append(version)
    type_id = convert_from_binary(line[from_index+3:from_index+6])
    from_index += 6
    if type_id == 4:
        number_bits = ''
        while True:
            bits = line[from_index:from_index + 5]
            number_bits += bits[1:]
            from_index += 5
            if bits[0] == '0':
                break
        number = convert_from_binary(number_bits)
        # print(number)
    else:
        length_type_bit = line[from_index:from_index+1]
        from_index += 1
        if length_type_bit == '0':
            length_bits = line[from_index:from_index + 15]
            from_index += 15
            length = convert_from_binary(length_bits)
            new_index = from_index
            while new_index < from_index + length:
                new_index = get_packet(line, new_index, versions)
            from_index = new_index
        else:
            number_of_subpackets_bits = line[from_index:from_index + 11]
            from_index += 11
            number_of_subpackets = convert_from_binary(number_of_subpackets_bits)
            for si in range(0, number_of_subpackets):
                from_index = get_packet(line, from_index, versions)
    return from_index


def run():
    hex_lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    for hex_line in hex_lines:
        print("-----")
        line = ''
        for hex_number in hex_line:
            line += hex_convertor[hex_number]
        versions = []
        from_index = get_packet(line, 0, versions)
        print(versions)
        print(sum(versions))
