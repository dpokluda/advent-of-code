def run():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    simple_digits = 0
    for line in lines:
        digits = line.split(" | ")[1].split(" ")
        for digit in digits:
            # print(f"{digit}: {len(digit)}")
            if len(digit) in [2, 3, 4, 7]:
                simple_digits += 1

    print(simple_digits)
