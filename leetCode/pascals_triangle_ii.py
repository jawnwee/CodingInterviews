def pascals_helper(rowIndex):
    if rowIndex == 1:
        return [1]
    if rowIndex == 2:
        return [1,2,1]
    result = pascals_helper(rowIndex-1)
    final = []
    final.append(1)
    previous = 1
    for i in xrange(1, len(result)):
        final.append(result[i] + previous)
        previous = result[i]
    final.append(1)
    return final

def getRow(rowIndex):
    if rowIndex == 0:
        return None
    return pascals_helper(rowIndex)
