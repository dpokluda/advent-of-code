import copy


def get_shortest_path(points, start, end):
    x = abs(end[0] - start[0] + 1)
    y = abs(end[1] - start[1] + 1)
    m = max(x, y)
    dx = x / m
    dy = y / m
    path = []
    px = end[1]
    py = end[0]
    for i in range(0, m):
        nx = int(start[0] + (i*dx))
        ny = int(start[1] + (i*dy))
        if px < nx and py < ny:
            for j in range(1, nx-px+1):
                path.append([px+j, py])
            for j in range(1, ny-py+1):
                path.append([nx, py+j])
        else:
            path.append([nx, ny])
        px = nx
        py = ny
    return path


directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def find_route(start, end, points, visited, risk, max_risk):
    risk += points[start[1]][start[0]]
    if risk > max_risk and start != end:
        return None
    risks = []
    for d in directions:
        nx = start[0] + d[0]
        ny = start[1] + d[1]
        if nx > 9 or ny > 9 or nx < 0 or ny < 0:
            continue
        if not visited[ny][nx]:
            visited_clone = copy.deepcopy(visited)
            visited_clone[ny][nx] = True
            r = find_route([nx, ny], end, points, visited_clone, risk, max_risk)
            if r is not None:
                print(r)
                risks.append(r)
    if len(risks) == 0:
        return None
    else:
        return min(risks)


def run():
    lines = [x.strip() for x in open('test.txt', 'r').readlines()]
    points = []
    for line in lines:
        points.append(list([int(x) for x in line]))

    sum = 0
    for point in get_shortest_path(points, [0, 0], [9, 9]):
        sum += points[point[1]][point[0]]
    print(sum)

    visited = [[False for _ in range(0, 10)] for _ in range(0, 10)]
    risk = find_route([0, 0], [9, 9], points, visited, -points[0][0], sum)
    print(risk)
