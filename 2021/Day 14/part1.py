def run():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    template = [x for x in lines[0]]
    rules = {}
    for index in range(2, len(lines)):
        items = lines[index].split(' -> ')
        rules[items[0]] = items[1]

    for step in range(0, 10):
        new_template = template[0]
        for index in range(0, len(template) - 1):
            new_template += rules.get(template[index] + template[index + 1]) + template[index + 1]
        # print(f'{len(new_template)}: {new_template}')
        template = new_template

    print(len(template))
    counts = {}
    for character in template:
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1

    max_count = -1
    min_count = -1
    for index, (character, count) in enumerate(counts.items()):
        if max_count < count or max_count == -1:
            max_count = count
        if min_count > count or min_count == -1:
            min_count = count

    print(f'{max_count} - {min_count} = {max_count - min_count}')
