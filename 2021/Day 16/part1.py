hex_convertor = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
       '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

def convert_from_binary(value):
    bits = [int(x) for x in value]
    # print(value)
    number = 0
    for i in range(0, len(bits)):
        number += bits[i] * 2 ** (len(bits) - i - 1)
    return number


sum_of_versions = 0


def convert_packet(line, sum_of_versions):
    version = convert_from_binary(line[:3])
    print(f'v={version}')
    sum_of_versions += version
    type_id = convert_from_binary(line[3:6])
    from_index = 6
    if type_id == 4:
        number_bits = ''
        while True:
            bits = line[from_index:from_index + 5]
            number_bits += bits[1:]
            from_index += 5
            if bits[0] == '0':
                break
        number = convert_from_binary(number_bits)
        print(number)
    else:
        length_type_bit = line[from_index:from_index + 1]
        from_index += 1
        if length_type_bit == '0':
            length_bits = line[from_index:from_index + 15]
            from_index += 15
            length = convert_from_binary(length_bits)
            subpacket1_bits = line[from_index:from_index + 11]
            from_index += 11
            sum_of_versions = convert_packet(subpacket1_bits, sum_of_versions)
            # print(subpacket1)
            subpacket2_bits = line[from_index:from_index + 16]
            from_index += 16
            sum_of_versions = convert_packet(subpacket2_bits, sum_of_versions)
            # print(subpacket)
        else:
            number_of_subpackets_bits = line[from_index:from_index + 11]
            from_index += 11
            number_of_subpackets = convert_from_binary(number_of_subpackets_bits)
            for si in range(0, number_of_subpackets):
                subpacket_bits = line[from_index:from_index + 11]
                from_index += 11
                sum_of_versions = convert_packet(subpacket_bits, sum_of_versions)
                # print(subpacket)
    return sum_of_versions


def run():
    hex_lines = [x.strip() for x in open('test.txt', 'r').readlines()]
    for hex_line in hex_lines:
        print("-----")
        line = ''
        for hex_number in hex_line:
            line += hex_convertor[hex_number]
        print(convert_packet(line, 0))
