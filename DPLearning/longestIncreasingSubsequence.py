def lis(arr):
    l = []
    for i in range(len(arr)):
        findMaxList = max( [l[j] for j in range(i) if l[j][-1] < arr[i]] or [ [] ], key=len)
        findMaxList.append(arr[i])
        l.append(findMaxList)
    return max(l, key=len)
