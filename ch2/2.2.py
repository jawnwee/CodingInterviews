from linkedList import Node

# Assume k is less than number of nodes
def removeKthNode(listNode, k):
    if listNode == None or k < 0:
        return None
    runner = listNode
    for i in range(k - 1):
        if runner.nextNode != None:
            runner = runner.nextNode
        else:
            return None

    while runner != None:
        listNode = listNode.nextNode
        runner = runner.nextNode

    return listNode.data


test = Node(3)
test.addToTail(4)
test.addToTail(5)
test.addToTail(5)
test.addToTail(3)
test.addToTail(6)
