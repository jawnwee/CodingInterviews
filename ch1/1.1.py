# Problem 1.1: implement algorithm to determine if a string has
# all unique characters

# Used data structure to store an array of 0s in list to represent ascii
# If a character has been shown more than once, this unique function will
# return false
characters = [0 for i in range(256)]

def unique(string):
    for char in string:
        index = ord(char)
        if not characters[index]:
            characters[index] = 1
        else:
            return False
    return True

# Problem 1.1 without using data structures

def uniqueWithoutDataStructure(string):
    for char1 in string:
         hit = 0
         for char2 in string:
             if char1 == char2:
                 hit += 1
             if hit >= 1:
                 return False
    return True

# Problem 1.1 very elegant way
# set returns the set of characters eliminating duplicates so when we check the length
# and it does not match the regular length of the string, this means there are dupes
# O(n) to create that set, must iterate through the string at least once
def hasAllUniqueCharSet(inputString):
    # using hash table (as a set datastrueture)
    if len(inputString) > 256: return False
    return len(set(inputString)) == len(inputString)

# Testing, usually good practice to do

testtrue = "abcdefghijklmnopqrstuvwxyz"
testfalse = "aabbccddeefghaklj;"

funclist = [unique, uniqueWithoutDataStructure, hasAllUniqueCharSet]

for function in funclist:
    print "testing function " + str(function)
    if function(testtrue):
        print "test 1 passed"
    else:
        print "test 1 failed"

    if not function(testfalse):
        print "test 2 pass"
    else:
        print "failed test 2"
