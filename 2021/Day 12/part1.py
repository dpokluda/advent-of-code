def add_to_graph(graph, point1, point2):
    if point1 not in graph:
        graph[point1] = []
    graph[point1].append(point2)


def clone_list(l):
    clone = l[:]
    return clone


def clone_dict(d):
    return d.copy()


def find_routes(graph, start, end, max_visit_count, current_route, visit_counts):
    routes = []
    current_route.append(start)
    visit_counts[start] = visit_counts.get(start) + 1
    if start == end:
        routes.append(current_route)
    else:
        for neighbor in graph.get(start):
            if visit_counts.get(neighbor) >= max_visit_count.get(neighbor) != -1:
                # we have visited the point enough times
                continue
            else:
                # it is a possible next step
                routes += find_routes(graph, neighbor, end, max_visit_count,
                                      clone_list(current_route), clone_dict(visit_counts))
    return routes


def create_max_visit_counts(visit_counts, point):
    if point not in visit_counts:
        if point in ['start', 'end']:
            visit_counts[point] = 1
        elif point.isupper():
            visit_counts[point] = -1
        else:
            visit_counts[point] = 1


def run():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    graph = {}
    max_visit_counts = {}
    visit_counts = {}
    for line in lines:
        point1, point2 = line.split("-")
        add_to_graph(graph, point1, point2)
        add_to_graph(graph, point2, point1)
        create_max_visit_counts(max_visit_counts, point1)
        create_max_visit_counts(max_visit_counts, point2)
        visit_counts[point1] = 0
        visit_counts[point2] = 0
    print(graph)

    routes = find_routes(graph, 'start', 'end', max_visit_counts, [], visit_counts)
    print(routes)
    print(len(routes))
