cached_counts = {}


def run():
    numbers = [int(x) for x in open('input.txt', 'r').readline().split(',')]
    print(numbers)
    positions = [[pos, 0] for pos in range(min(numbers), max(numbers) + 1)]
    fuel_by_position_change = [[pos, 0] for pos in range(min(numbers), max(numbers) + 1)]
    for change in fuel_by_position_change:
        fuel = 0
        for step in range(1, change[0] + 1):
            fuel += step
        change[1] = fuel

    for position in positions:
        for number in numbers:
            position[1] += fuel_by_position_change[abs(position[0] - number)][1]

    minimum_position = positions[0][0]
    minimum_fuel = positions[0][1]
    for position in positions:
        if position[1] < minimum_fuel:
            minimum_position = position[0]
            minimum_fuel = position[1]
    print(minimum_position)
    print(minimum_fuel)
