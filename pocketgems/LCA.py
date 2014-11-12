class Result:
    def __init__(self, node, isLCA = False):
        self.isLCA = isLCA
        self.node = node

def findLCA(root, first, second):
    if root is None:
        return Result(None, False)
        # Not sure what to do here
    if root == first and root == second:
        return root

    Result left = self.findLCA(root.left, first, second)
    if left.isLCA:
        return left

    Result right = self.findLCA(root.right, first, second)
    if right.isLCA:
        return right

    if right.node and left.node:
        return Result(root, True)

    elif right.node == root or left.node == root:
        is_ancestor = False
        if right.node or left.node:
            is_ancestor = True
        return Result(root, is_ancestor)

    else:
        if right.node:
            return Result(right.node, False)
        return Result(left.node, False)
