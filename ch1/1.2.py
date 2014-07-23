def reverse(x):
    s =[] 
    for c in x:
        if c:
            s.append(c)
    result = ''
    while not len(s) == 0:
        c = s.pop()
        result+=c
    return result

def reverse_recursive(x):
    if len(x) == 1:
        return x
    else:
        return reverse_recursive(x[1:]) + x[0]
