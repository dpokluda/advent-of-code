rules = {}


def update_counts(character, counts):
    if character in counts:
        counts[character] += 1
    else:
        counts[character] = 1


def calculate_counts(first, second, level, counts):
    key = rules.get(first + second)
    update_counts(key, counts)
    if level < 30:
        calculate_counts(first, key, level + 1, counts)
        calculate_counts(key, second, level + 1, counts)


def run():
    lines = [x.strip() for x in open('test.txt', 'r').readlines()]
    template = [x for x in lines[0]]
    for index in range(2, len(lines)):
        items = lines[index].split(' -> ')
        rules[items[0]] = items[1]

    counts = {}
    # for character in template:
    #     update_counts(character, counts)

    patterns = {}
    for index, (key, count) in enumerate(rules.items()):
        print(index)
        rule_counts = {}
        calculate_counts(key[0], key[1], 1, rule_counts)
        patterns[key] = rule_counts

    for index in range(0, len(template) - 1):
        update_counts(template[index], counts)
        pattern_counts = patterns.get(template[index] + template[index + 1])
        for index, (key, count) in enumerate(pattern_counts.items()):
            if key in counts:
                counts[key] += count
            else:
                counts[key] = count
    counts[template[len(template)-1]] += 1

    max_count = -1
    min_count = -1
    for index, (key, count) in enumerate(counts.items()):
        if max_count < count or max_count == -1:
            max_count = count
        if min_count > count or min_count == -1:
            min_count = count

    print(f'{max_count} - {min_count} = {max_count - min_count}')
