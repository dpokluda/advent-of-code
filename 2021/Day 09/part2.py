def get_neighbors(numbers, row, col):
    if numbers[row][col] in [9, -1]:
        return []
    point = numbers[row][col]
    numbers[row][col] = -1
    neighbors = [point]
    if row > 0 and numbers[row - 1][col] not in [9, -1]:
        neighbors += get_neighbors(numbers, row - 1, col)
    if row < len(numbers) - 1 and numbers[row + 1][col] not in [9, -1]:
        neighbors += get_neighbors(numbers, row + 1, col)
    if col > 0 and numbers[row][col - 1] not in [9, -1]:
        neighbors += get_neighbors(numbers, row, col - 1)
    if col < len(numbers[0]) - 1 and numbers[row][col + 1] not in [9, -1]:
        neighbors += get_neighbors(numbers, row, col + 1)
    return neighbors


def run():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    numbers = []
    for line in lines:
        numbers.append([int(x) for x in line])

    basins = []
    for row in range(0, len(numbers)):
        for col in range(0, len(numbers[row])):
            current = get_neighbors(numbers, row, col)
            if len(current) > 0:
                basins.append(current)
                # print(current)
                # print(len(current))

    basins.sort(key=lambda x: -len(x))
    print(len(basins[0]) * len(basins[1] * len(basins[2])))
