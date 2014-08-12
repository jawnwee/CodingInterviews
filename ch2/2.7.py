from linkedList import Node

def isListPalindrome(list_head):
    if list_head == None:
        return 'List is empty'
    reversed_list = reverse_linkedList(list_head)
    current_list = list_head
    while current_list != None:
        if reversed_list.data != current_list.data:
            return False
        reversed_list = reversed_list.nextNode
        current_list = current_list.nextNode
    return True

def reverse_linkedList(list_head):
    rev_list = Node(list_head.data)
    list_head = list_head.nextNode()
    while list_head != None:
        rev_list.addNodeToFront(list_head.data)
        list_head = list_head.nextNode()
    return rev_list
