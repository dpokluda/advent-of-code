def run():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    numbers = []
    for line in lines:
        numbers.append([int(x) for x in line])

    points = []
    for row in range(0, len(numbers)):
        for col in range(0, len(numbers[row])):
            point = numbers[row][col]
            neighbors = []
            if row > 0:
                neighbors.append(numbers[row-1][col])
            if row < len(numbers) - 1:
                neighbors.append(numbers[row+1][col])
            if col > 0:
                neighbors.append(numbers[row][col-1])
            if col < len(numbers[0]) - 1:
                neighbors.append(numbers[row][col+1])
            points.append([point, neighbors])

    sum = 0
    for point in points:
        if point[0] < min(point[1]):
            sum += (1 + point[0])
    print(sum)
