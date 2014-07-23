def rotateNinety(matrix, n):
    result = []
    for i in range(n):
        result.append([])
        for j in range(n):
            result[i].append(0)
    for i in range(n):
        for j in range(n):
            result[j][(n-1)-i] = matrix[i][j]
    return result

def improvedRotateNinety(matrix, n):
    for layer in range(n/2):
        first = layer
        last = n - 1 - layer
        print("first", first)
        for i in xrange(first, last):
            print(i)
            offset = i - first
            temp = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last-offset][first] = matrix[last][last-offset]
            matrix[last][last-offset] = matrix[i][last]
            matrix[i][last] = temp
            print(matrix)
    return matrix

