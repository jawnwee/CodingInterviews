from Tree import Tree

def pre_order(Tree t):
    if t.right == None and t.left == None:
        return t.data
    elif t.right == None:
        return pre_order(t.left)
    elif t.left == None:
        return pre_order(t.right)
    print(t.data)
    print(pre_order(t.left))
    print(pre_order(t.right))

def in_order(Tree t):
    if t.right == None and t.left == None:
        return t.data
    elif t.right == None:
        return in_order(t.left)
    elif t.left == None:
        return in_order(t.right)
    print(in_order(t.left))
    print(t.data)
    print(in_order(t.right))

def post_order(Tree t):
    if t.right == None and t.left == None:
        return t.data
    elif t.right == None:
        return post_order(t.left)
    elif t.left == None:
       return post_order(t.right)
    print(post_order(t.left))
    print(post_order(t.right))
    print(t.data)
