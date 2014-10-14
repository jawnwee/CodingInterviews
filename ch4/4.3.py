from Tree import Tree

def min_height_bst(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return Tree(arr[0])
    root = Tree(arr[len(arr) / 2])
    left = min_height_bst(arr[:len(arr)/2])
    right = min_height_bst(arr[len(arr)/2 + 1:])
    if left != None:
        root.left = left
    if right != None:
        root.right = right
    return root

test = [2,3,4,5,6,7,8,9]
