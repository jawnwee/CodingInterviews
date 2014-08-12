from linkedList import Node

def removeDuplicates(node):
    if node is None:
        return None
    listSet = []
    listSet.append(node.data)
    while node.nextNode != None:
        current = node.nextNode.data
        if current not in listSet:
            listSet.append(current)
            node = node.nextNode
        else:
            if node.nextNode.nextNode:
                node.nextNode = node.nextNode.nextNode
            else:
                node.nextNode = None

def removeDuplicatesNoBuffer(node):
    if node is None:
        return None
    while node != None:
        current = node
        while current.nextNode != None:
            if current.nextNode.data == node.data:
                current.nextNode = current.nextNode.nextNode
            else:
                current = current.nextNode
        node = node.nextNode


test = Node(3)
test.addToTail(4)
test.addToTail(5)
test.addToTail(5)
test.addToTail(3)
test.addToTail(6)
