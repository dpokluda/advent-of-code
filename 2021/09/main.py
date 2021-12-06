def run():
    file = open('input.txt', 'r')
    lines = file.readlines()

    # load coordinates
    numbers = []
    for line in lines:
        points = [p.strip() for p in line.strip().split("->")]
        for point in points:
            numbers.append([int(c) for c in point.split(",")])
    number_of_rows = max(n[0] for n in numbers) + 1
    number_of_cols = max(n[1] for n in numbers) + 1

    # create empty map
    map = []
    for r in range(0, number_of_rows):
        row = []
        for c in range(0, number_of_cols):
            row.append(0);
        map.append(list(row))

    # draw lines
    for index in range(0, len(numbers) // 2):
        begin = numbers[index*2]
        end = numbers[index*2 + 1]
        if begin[0] == end[0]:
            # row
            row = begin[0]
            for col in range(min(begin[1], end[1]), max(begin[1], end[1]) + 1):
                map[row][col] += 1
        elif begin[1] == end[1]:
            # col
            col = begin[1]
            for row in range(min(begin[0], end[0]), max(begin[0], end[0]) + 1):
                map[row][col] += 1
        else:
            continue

    # count intersections
    count = 0
    for row in map:
        for col in row:
            if col > 1:
                count += 1

    print(count)


if __name__ == '__main__':
    run()
