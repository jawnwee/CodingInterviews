def stringCompression(word):
    result = ''
    if len(word) == 0:
        return ''
    else:
        count = 1
        previous = word[0]
        for i in range(1,len(word)):
            current = word[i]
            if current == previous:
                count += 1
            else:
                compress = previous + str(count)
                result += compress
                count = 1
                previous = current
        if count != 0:
            compress = previous + str(count)
            result += compress
        if len(result) >= len(word):
            return word
    return result
