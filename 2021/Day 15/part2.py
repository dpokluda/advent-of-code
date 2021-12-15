directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
multiplier = 10000


def to_hash(point):
    return point[0] * multiplier + point[1]


def from_hash(value):
    return [value // multiplier, value % multiplier]


def run_djikstra(start, end, costs, risks):
    to_visit = set()
    to_visit.add(to_hash(start))
    while len(to_visit) > 0:
        print(len(to_visit))
        new_to_visit = set()
        for point_hash in to_visit:
            point = from_hash(point_hash)
            px = point[0]
            py = point[1]
            for d in directions:
                nx = px + d[0]
                ny = py + d[1]
                if nx > end[0] or ny > end[1] or nx < 0 or ny < 0:
                    continue
                if costs[ny][nx] is None or costs[ny][nx] > costs[py][px] + risks[ny][nx]:
                    costs[ny][nx] = costs[py][px] + risks[ny][nx]
                    hash_value = to_hash([nx, ny])
                    if hash_value not in new_to_visit:
                        new_to_visit.add(hash_value)

        to_visit = new_to_visit


def run():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    template = []
    template_size_x = len(lines[0])
    template_size_y = len(lines)
    for line in lines:
        template.append(list([int(x) for x in line]))

    risks = []
    for row in range(0, template_size_y * 5):
        offset_row = row // template_size_y
        risks_row = []
        for col in range(0, template_size_x * 5):
            offset_col = col // template_size_x
            offset = offset_row + offset_col
            value = (template[row % template_size_y][col % template_size_x] + offset)
            while value > 9:
                value -= 9
            risks_row.append(value)
        risks.append(risks_row)

    size_x = len(risks[0])
    size_y = len(risks)
    start = [0, 0]
    end = [size_x - 1, size_y - 1]
    print(end)

    costs = [[None for _ in range(0, size_x)] for _ in range(0, size_y)]
    costs[0][0] = 0
    run_djikstra(start, end, costs, risks)

    print(costs[end[1]][end[0]])
