from Tree import Tree

t1_in = ''
t1_pre = ''
t2_in = ''
t2_pre = ''

def pre_order_string_t1(tree):
    global t1_pre
    if tree == None:
        return t1_pre
    if tree.data == None:
        t1_pre += '0'
    else:
        t1_pre += str(tree.data)
        print('current tree', t1_pre)
    pre_order_string_t1(tree.left)
    pre_order_string_t1(tree.right)

def in_order_string_t1(tree):
    global t1_in
    if tree == None:
        return t1_in
    if tree.left == None and tree.right == None:
        if tree.data == None:
            t1_in += '0'
        else:
            t1_in += str(tree.data)
        return t1_in
    else:
        in_order_string_t1(tree.left)
        t1_in += str(tree.data)
        in_order_string_t1(tree.right)

def pre_order_string_t2(tree):
    global t2_pre
    if tree == None:
        return t2_pre
    if tree.data == None:
        t2_pre += '0'
    else:
        t2_pre += str(tree.data)
        print('current tree', t2_pre)
    pre_order_string_t2(tree.left)
    pre_order_string_t2(tree.right)

def in_order_string_t2(tree):
    global t2_in
    if tree == None:
        return t2_in
    if tree.left == None and tree.right == None:
        if tree.data == None:
            t2_in += '0'
        else:
            t2_in += str(tree.data)
        return t2_in
    else:
        in_order_string_t2(tree.left)
        t2_in += str(tree.data)
        in_order_string_t2(tree.right)

def treeMatch(t1, t2):
    in_order_string_t1(t1)
    pre_order_string_t1(t1)
    in_order_string_t2(t2)
    pre_order_string_t2(t2)
    print('t1 in:' , t1_in, 't1_pre', t1_pre)
    print('t2 in:' , t2_in, 't2_pre', t2_pre)
    if t2_in in t1_in and t2_pre in t1_pre:
        return True
    return False

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

sthree = Tree(3)
sfour = Tree(4)
sone = Tree(1)

sthree.left = sone
sthree.right = sfour
