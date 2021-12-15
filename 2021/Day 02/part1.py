def run():
    lines = [x.strip().split(' ') for x in open('input.txt', 'r').readlines()]

    horizontal = 0
    vertical = 0
    for line in lines:
        if line[0] == 'forward':
            horizontal += int(line[1])
        elif line[0] == 'down':
            vertical += int(line[1])
        elif line[0] == 'up':
            vertical -= int(line[1])
        else:
            raise Exception(f'Unknown command: {line[0]}')

    print(horizontal * vertical)
