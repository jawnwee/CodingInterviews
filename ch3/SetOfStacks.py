from SQDS import Stack

class SetOfStacks():

    def __init__(self, cap):
        self.stacks = []
        self.capacity = cap

    def push(self, data):
        lengthOfSet = len(self.stacks)
        indexOfUnfilledStack = None
        for i in range(0, lengthOfSet):
            if self.stacks[i].stackSize() < self.capacity:
                indexOfUnfilledStack = i
                break
        if indexOfUnfilledStack != None:
            self.stacks[indexOfUnfilledStack].push(data)
        else:
            self.stacks.append(Stack())
            self.stacks[lengthOfSet].push(data)

    def pop(self):
        if self.stacks == []:
            return 'Set of Stacks is Empty'
        lengthOfSet = len(self.stacks) - 1
        if self.stacks[lengthOfSet].stackSize() > 0:
            value = self.stacks[lengthOfSet].pop()
            if self.stacks[lengthOfSet].stackSize() == 0:
                self.stacks.pop()
            return value

    def popAt(self, index):
        if index > len(self.stacks) - 1:
            return 'There arent this many stacks'
        value = self.stacks[index].pop()
        if self.stacks[index].stackSize() == 0:
            self.stacks.pop(index)
