def distinct(arr):
    max_len, start, end, r_start, r_end = 0, 0, 0, 0, 0
    d = {}
    for i in xrange(len(arr)):
        if arr[i] in d:
            prev = d[arr[i]]
            d[arr[i]] = i
            start = prev + 1
        else:
            d[arr[i]] = i
            end = i
            l = end - start
            if l > max_len:
                r_start = start
                r_end = end
                max_len = l
    return (r_start, r_end)
