def run():
    file = open('input.txt', 'r')
    data = [int(line) for line in file.readlines()]

    count = 0
    for index in range(3, len(data)):
        window1 = data[index - 3] + data[index - 2] + data[index - 1]
        window2 = data[index - 2] + data[index - 1] + data[index]
        if window1 < window2:
            count += 1

    print(count)
