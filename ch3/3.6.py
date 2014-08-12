from SQDS import Stack

def sortStack(stack):
    if stack.isEmpty():
        return 'Stack is empty'
    less = Stack()
    middle = Stack()
    greater = Stack()
    return sortStackHelper(stack, less, middle, greater)

def sortStackHelper(stack, less, middle, greater):
    if stack.isEmpty():
        return Stack()
    middle.push(stack.pop())
    if stack.isEmpty():
        return middle
    while not stack.isEmpty():
        data = stack.pop()
        if data >= middle.peek():
            greater.push(data)
        else:
            less.push(data)
    leftHand = sortStackHelper(less, Stack(), Stack(), Stack())
    rightHand = sortStackHelper(greater, Stack(), Stack(), Stack())
    leftHand.push(middle.pop())
    while not rightHand.isEmpty():
        middle.push(rightHand.pop())
    while not middle.isEmpty():
        leftHand.push(middle.pop())
    return leftHand
