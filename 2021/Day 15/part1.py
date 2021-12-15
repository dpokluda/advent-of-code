directions = [[1, 0], [0, 1]]  # , [-1, 0], [0, -1]]


def run_djikstra(start, end, costs, risks):
    to_visit = [start]
    while len(to_visit) > 0:
        print(to_visit[0], len(to_visit))
        new_to_visit = []
        for point in to_visit:
            px = point[0]
            py = point[1]
            for d in directions:
                nx = px + d[0]
                ny = py + d[1]
                if nx > end[0] or ny > end[1] or nx < 0 or ny < 0:
                    continue
                if [nx, ny] not in new_to_visit:
                    new_to_visit.append([nx, ny])
                if costs[ny][nx] is None or costs[ny][nx] > costs[py][px] + risks[ny][nx]:
                    costs[ny][nx] = costs[py][px] + risks[ny][nx]
        to_visit = new_to_visit


def run():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    risks = []
    for line in lines:
        risks.append(list([int(x) for x in line]))

    size_x = len(lines[0])
    size_y = len(lines)
    start = [0, 0]
    end = [size_x - 1, size_y - 1]

    costs = [[None for _ in range(0, size_x)] for _ in range(0, size_y)]
    costs[0][0] = 0
    run_djikstra(start, end, costs, risks)

    print(costs[end[1]][end[0]])
