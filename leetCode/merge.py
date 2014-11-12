def merge(A, m, B, n):
    i = 0
    b = 0
    while i < m:
        if b < n:
            if A[i] > B[b]:
                if i == 0:
                    A.insert(0, B[b])
                else:
                    A.insert(i, B[b])
                b += 1
                i += 1
        i += 1
    if b != n:
        for j in range(b, n):
            A.insert(len(A),B[j])
    return A
