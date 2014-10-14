from Tree import Tree
from Queue import Queue

q = Queue()
result = []

def find_d_lists(bst):
    q.enqueue(bst)
    find_d_lists_helper()

def find_d_lists_helper():
    if q.isEmpty():
        return
    result.append(q)
    current_level = []
    while not q.isEmpty():
        current_level.append(q.dequeue())
    print(current_level)
    for child in current_level:
        if child.left != None:
            q.enqueue(child.left)
        if child.right != None:
            q.enqueue(child.right)
    return find_d_lists_helper()

one = Tree(1)
three = Tree(3)
four = Tree(4)
five = Tree(5)
six = Tree(6)
seven = Tree(7)
eight = Tree(8)

five.left = three
five.right = seven

three.right = four
three.left = one

seven.left = six
seven.right = eight
