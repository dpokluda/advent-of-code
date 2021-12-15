import copy
l = [[1, 2], [3, 4]]
c = copy.deepcopy(l)
l[1][1] = 0
print(c)
