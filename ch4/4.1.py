from Tree import Tree

def isBalanced(t):
    result = heightOfTree(t)
    if result == -1:
        return False

    return True

def heightOfTree(t):
    if t == None  or t.right == None and t.left == None:
        return 0
    heightOfLeft = heightOfTree(t.left)
    heightOfRight = heightOfTree(t.right)
    if heightOfLeft == -1 or heightOfRight == -1 or abs(heightOfLeft - heightOfRight) > 1:
        return -1
    return max(heightOfLeft, heightOfRight) + 1

a = Tree(15)
b = Tree(20)
c = Tree(30)
d = Tree(5)
e = Tree(12)
f = Tree(13)
b.left = a
b.right = c
a.left = d
a.right = e
e.right = f
