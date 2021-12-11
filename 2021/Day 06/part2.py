cached_counts = {}


def fish_population(age, days):
    if (age, days) in cached_counts:
        return cached_counts[(age, days)]
    d = days - age - 1
    count = 1
    while d >= 0:
        count += fish_population(8, d)
        d -= 7
    cached_counts[(age, days)] = count
    return count


def run():
    numbers = [int(x) for x in open('input.txt', 'r').readline().split(',')]
    gens = {}
    for days in range(0, 6):
        gens[days] = fish_population(days, 256)
        print(f"  {days}: {gens.get(days)}")

    count = 0
    for number in numbers:
        count += gens.get(number)

    print(count)
