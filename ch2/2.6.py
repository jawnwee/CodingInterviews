from linkedList import Node

def duplicateFinder(head):
    if head == None:
        return 'List is empty'
    f_list = head
    s_list = head
    finder_list = head
    while f_list.data != s_list.data:
        f_list = f_list.nextNode
        s_list = s_list.nextNode
        s_list = s_list.nextNode
        if f_list == None or s_list == None:
            return 'Not a ciruclar linked list'
    while f_list.data != finder_list.data:
        f_list = f_list.nextNode
        finder_list = finder_list.nextNode
    return finder_list.data
