from linkedList import Node

def removeMiddleNode(middle):
    if middle == None:
        return 'Cannot remove a "None" node'
    if middle.next == None:
        return 'Next middle node does not extist'
    middle.data = middle.nextNode.data
    if middle.nextNode.nextNode != None:
        middle.nextNode = middle.nextNode.nextNode
    else:
        middle.nextNode = None

test = Node(3)
test.addToTail(4)
test.addToTail(5)
test.addToTail(5)
test.addToTail(3)
test.addToTail(6)
