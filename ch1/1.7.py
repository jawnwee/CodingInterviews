def setZeroHelper(m, n):
    return 0.5 * (m + n) * (m + n + 1) + n

def setZero(matrix, m, n):
    visitedIndices = []
    for i in range(m):
        for j in range(n):
            index = setZeroHelper(i, j)
            print(matrix[i][j], i, j)
            if matrix[i][j] == 0 and index not in visitedIndices:
                for n_second in range(n):
                    matrix[i][n_second] = 0
                    visitedIndices.append(setZeroHelper
                            (i, n_second))
                for m_second in range(m):
                    matrix[m_second][j] = 0
                    visitedIndices.append(setZeroHelper
                            (m_second, j))
            else:
                visitedIndices.append(index)
    return matrix
