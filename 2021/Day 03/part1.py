def run():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    lines_bits = []
    for line in lines:
        lines_bits.append([int(c) for c in line])

    gamma_rate = 0
    epsilon_rate = 0
    for index in range(0, len(lines_bits[0])):
        if [line[index] for line in lines_bits].count(1) * 2 > len(lines_bits):
            gamma_rate += 2**(len(lines_bits[0])-index-1)
        if [line[index] for line in lines_bits].count(0) * 2 > len(lines_bits):
            epsilon_rate += 2**(len(lines_bits[0])-index-1)
    # print(gamma_rate)
    # print(epsilon_rate)
    print(gamma_rate * epsilon_rate)
