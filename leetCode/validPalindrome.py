def isPalindrome(s):
    alph_char = ''
    for c in s:
        char_value = ord(c)
        if (char_value >= 65 and char_value <= 90) or (char_value >= 97 and char_value <= 122):
            print 'bleh'
            alph_char += c
    if alph_char == '':
        return True
    alph_length = len(alph_char)
    alph_char = alph_char.lower()
    for i in xrange(alph_length/2):
        print(alph_char[i])
        if alph_char[i] != alph_char[alph_length - i - 1]:
            return False
    return True

def improvedIsPalindrome(s):
    l = [x.lower() for x in s if x.isalnum()]
    if l:
        result = True if l == list(reversed(l)) else False
        return result
    else:
        return True
