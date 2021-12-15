def run():
    numbers = [int(x) for x in open('input.txt', 'r').readline().split(',')]
    fishes = []
    for number in numbers:
        fishes.append([number, 0])
    print(fishes)

    number_of_days = 80

    for day in range(1, number_of_days + 1):
        if day % 10 == 0:
            print(day)
        for fish in fishes:
            if fish[1] != day:
                fish[0] -= 1
                if fish[0] == -1:
                    fish[0] = 6
                    fishes.append([8, day])
        # print(fishes)

    print(len(fishes))
