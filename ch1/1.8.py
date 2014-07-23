def isSubstring(w1, w2):
    return w1 in w2

def isRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        wordLength = len(s1) - 1
        i, j = 0, 0
        while i != wordLength and j != wordLength:
            print(i, j)
            if s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                j += 1
        ending_difference = wordLength - i
        word = s2[ending_difference:] + s2[0:i]
        return isSubstring(word, s1)

### Could have just added the first string twice. and check if this string is substring of second; its a fantastic solution ###
