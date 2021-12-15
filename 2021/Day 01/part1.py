def run():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    data = [int(x) for x in lines]

    count = 0
    for index in range(0, len(data)-1):
        if data[index+1] > data[index]:
            count += 1

    print(count)
