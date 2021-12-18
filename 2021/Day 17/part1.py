from math import sqrt


def next_step(position, velocity):
    position[0] += velocity[0]
    position[1] += velocity[1]
    velocity[0] += -1 if velocity[0] > 0 else 1 if velocity[0] < 0 else 0
    velocity[1] -= 1


def hit_target(x, y, vx, vy, target_x, target_y):
    max_y = 0
    point = [x, y]
    velocity = [vx, vy]
    while True:
        next_step(point, velocity)
        if target_x[0] <= point[0] <= target_x[1] and target_y[0] <= point[1] <= target_y[1]:
            return [True, max_y]
        elif target_x[1] < point[0] or point[1] < target_y[0]:
            return [False, None]
        if max_y < point[1]:
            max_y = point[1]


def run():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    area = lines[0].split(': ')[1].split(', ')
    x = [int(x) for x in area[0].split('=')[1].split('..')]
    y = [int(y) for y in area[1].split('=')[1].split('..')]
    x.sort()
    y.sort()

    print('Target:')
    print(x, y)

    mvx = 0
    mvy = 0
    my = 0
    print('Hits:')
    for n in range(1, x[1]):
        # vy + vy-1 + vy-2 + ... + vy-(n-1) = y => vy_to
        vy_from = 1/4*(sqrt(9*n**2 + 4*n*y[0] - 18*n + 4*y[0]**2 - 4*y[0] + 9) + n + 2*y[0] - 1) // 1
        vy_to = 1/4*(sqrt(9*n**2 + 4*n*y[1] - 18*n + 4*y[1]**2 - 4*y[1] + 9) + n + 2*y[1] - 1) // 1 + 1
        vx_stop = 1/2*(sqrt(8*n + 1) - 1) // 1

        for vy in range(int(vy_from), int(vy_to+1)):
            for vx in range(int(vx_stop), x[0]):
                is_hit, hmy = hit_target(0, 0, vx, vy, x, y)
                if is_hit:
                    print(vx, vy, n, hmy)
                if is_hit and hmy > my:
                    my = hmy
                    mvx = vx
                    mvy = vy

    print('Maximum:')
    print(mvx, mvy, my)
