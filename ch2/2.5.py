from linkedList import Node

# Assume no negative number
def sumLinkedListReverse(first, second):
    if first == None and second == None:
        return None
    carry = 0
    result = None
    while first != None or second != None or carry != 0:
        digit_sum = carry
        if first != None:
            digit_sum += first.data
            first = first.nextNode
        if second != None:
            digit_sum += second.data
            second = second.nextNode
        if result == None:
            result = Node(digit_sum%10)
        else:
            result.addToTail(digit_sum%10)
        carry = digit_sum / 10
    return result

def sumLinkedListForward(first, second):
     first_list = reverseLinkedList(first)
     second_list = reverseLinkedList(second)
     return sumLinkedListReverse(first_list, second_list)


def reverseLinkedList(linkedList):
    result = None
    while linkedList != None:
        data = linkedList.data
        if result == None:
            result = Node(data)
        else:
            node = Node(data)
            node.nextNode = result
            result = node
        linkedList = linkedList.nextNode
    return result


first_test = Node(7)
first_test.addToTail(1)
first_test.addToTail(6)

second_test = Node(5)
second_test.addToTail(9)
second_test.addToTail(2)
