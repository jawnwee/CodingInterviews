def insertSpaces(word):
    charList = []
    for c in word:
        if c == ' ':
            c = '%20'
        charList.append(c)
    print('word', ''.join(charList))


def replaceSpace(string):
    charList = []
    for char in string:
        print('char, string', len(charList), len(string))
        if len(charList) == len(string):
            break
        if char == ' ':
            charList.append('%')
            charList.append('2')
            charList.append('0')
        else:
            charList.append(char)
    return ''.join(charList)
