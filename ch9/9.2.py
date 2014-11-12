memoize = [ [0 for i in range(10)] for i in range(10) ]

def robot_possible_moves(x, y):
    global memoize
    if x < 0 or y < 0:
        return 0
    if memoize[x][y] > 0:
        return memoize[x][y]
    elif x == 0 and y == 0:
        return 1
    memoize[x][y] = robot_possible_moves(x - 1, y) + robot_possible_moves(x, y - 1)
    return memoize[x][y]


