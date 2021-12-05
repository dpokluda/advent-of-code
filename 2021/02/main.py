def run():
    file = open('input.txt', 'r')
    data = [int(line) for line in file.readlines()]
    i = 0
    count = 0
    while i <= len(data):
        if i >= 4:
            window1 = data[i-4] + data[i-3] + data[i-2]
            window2 = data[i-3] + data[i-2] + data[i-1]
            # print(window1)
            # print(window2)
            # print()
            if window1 < window2:
                count += 1
        i += 1
    print(count)


if __name__ == '__main__':
    run()
