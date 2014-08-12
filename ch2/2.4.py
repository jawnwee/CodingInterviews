from linkedList import Node

def partition(headNode, x):
    less_list = None
    greater_list = None
    if headNode == None:
        return 'cannot partition empty linkedlist'
    while headNode != None:
        current_data = headNode.data
        if current_data < x:
            if less_list == None:
                less_list = Node(current_data)
            else:
                less_list.addToTail(current_data)
        else:
            if greater_list == None:
                greater_list = Node(current_data)
            else:
                greater_list.addToTail(current_data)
        headNode = headNode.nextNode
    if less_list == None:
        return greater_list
    elif greater_list == None:
        return less_list
    else:
        less_list.addNodeToTail(greater_list)
        result = less_list
        return result

test = Node(3)
test.addToTail(4)
test.addToTail(5)
test.addToTail(5)
test.addToTail(3)
test.addToTail(6)
