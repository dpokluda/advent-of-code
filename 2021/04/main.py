def get_command_value(line):
    index = line.find(" ")
    return int(line[index+1:])


def run():
    file = open('input.txt', 'r')
    lines = file.readlines()
    horizontal = 0
    vertical = 0
    aim = 0
    for line in lines:
        value = get_command_value(line)
        if "forward" in line:
            horizontal += value
            vertical += (aim * value)
        elif "down" in line:
            aim += value
        elif "up" in line:
            aim -= value
        else:
            print(f"Unknown command: {line}")

    # print(f"Horizontal position: {horizontal}")
    # print(f"Vertical position: {vertical}")
    print(horizontal * vertical)


if __name__ == '__main__':
    run()
