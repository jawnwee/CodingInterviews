def countAndSay(n):
  result = '1'
  for i in range(n-1):
    new_result = ''
    length = len(result)
    prev = result[0]
    count = 1
    for c in range(1, length):
      if result[c] == prev:
        count += 1
      else:
        new_result += str(count)
        new_result += prev
        prev = result[c]
        count = 1
    new_result += str(count)
    new_result += prev
    result = new_result
  return result
