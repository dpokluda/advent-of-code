cached_counts = {}


def run():
    numbers = [int(x) for x in open('input.txt', 'r').readline().split(',')]
    print(numbers)
    positions = [[pos, 0] for pos in range(min(numbers), max(numbers) + 1)]
    for position in positions:
        for number in numbers:
            position[1] += abs(position[0] - number)

    minimum_position = positions[0][0]
    minimum_fuel = positions[0][1]
    for position in positions:
        if position[1] < minimum_fuel:
            minimum_position = position[0]
            minimum_fuel = position[1]
    print(minimum_position)
    print(minimum_fuel)
