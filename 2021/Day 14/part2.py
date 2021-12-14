def update_counts(key, counts, count):
    if key in counts:
        counts[key] += count
    else:
        counts[key] = count


def run():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    template = [x for x in lines[0]]
    rules = {}
    for index in range(2, len(lines)):
        items = lines[index].split(' -> ')
        rules[items[0]] = items[1]

    pair_counts = {}
    for index in range(0, len(template) - 1):
        update_counts(template[index] + template[index + 1], pair_counts, 1)

    for step in range(0, 40):
        new_pair_counts = {}
        for index, (key, count) in enumerate(pair_counts.items()):
            insert = rules.get(key)
            update_counts(key[0] + insert, new_pair_counts, count)
            update_counts(insert + key[1], new_pair_counts, count)
        pair_counts = new_pair_counts

    counts = {}
    for index, (key, count) in enumerate(pair_counts.items()):
        update_counts(key[1], counts, count)
    counts[template[0]] -= 1

    max_count = -1
    min_count = -1
    for index, (key, count) in enumerate(counts.items()):
        if max_count < count or max_count == -1:
            max_count = count
        if min_count > count or min_count == -1:
            min_count = count

    print(f'{max_count} - {min_count} = {max_count - min_count}')
