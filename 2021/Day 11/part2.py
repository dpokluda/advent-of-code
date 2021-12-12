def flash(numbers, row, col):
    new_flashes = 1
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0 or \
                    col+dx < 0 or col+dx > 9 or \
                    row+dy < 0 or row+dy > 9:
                continue
            if numbers[row+dy][col+dx] not in [-1, -2]:
                numbers[row+dy][col+dx] += 1
                if numbers[row+dy][col+dx] > 9:
                    numbers[row+dy][col+dx] = -2
                    new_flashes += flash(numbers, row+dy, col+dx)
    return new_flashes


def run():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    numbers = []
    for line in lines:
        numbers.append(list(int(x) for x in line))

    for row in range(0, len(lines)):
        print(numbers[row])

    flashes = 0
    step = 0
    while True:
        step += 1
        for row in range(0, len(lines)):
            for col in range(0, len(lines[0])):
                if numbers[row][col] != -1:
                    numbers[row][col] += 1
                    if numbers[row][col] > 9:
                        numbers[row][col] = -1
        for row in range(0, len(lines)):
            for col in range(0, len(lines[0])):
                if numbers[row][col] == -1:
                    flashes += flash(numbers, row, col)
        for row in range(0, len(lines)):
            numbers[row] = [0 if x > 9 or x in [-1, -2] else x for x in numbers[row]]
        not_flash = []
        for line in numbers:
            for number in line:
                if number != 0:
                    not_flash.append(number)
        if len(not_flash) == 0:
            print(step)
            break
