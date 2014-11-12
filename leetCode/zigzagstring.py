def convert(s, nRows):
    if nRows == 0 or nRows == 1:
        return s
    num_full_rows = (len(s) / nRows) + 1
    numCols = num_full_rows + (num_full_rows - 1) * (nRows - 2)
    rows = [ [ '' for c in range(numCols) ] for i in range(nRows)]
    row = 0
    col = 0
    for c in s:
        rows[row][col] = c
        if col%(nRows - 1) == 0 and row != nRows:
            row += 1
        else:
            row -= 1
            col += 1
        if row == nRows:
            row -= 2
            col += 1
    result = ''
    for row in rows:
        for letter in row:
            result += letter
    return result
