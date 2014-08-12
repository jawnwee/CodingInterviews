from SQDS import Stack

class Hannoi():

    def __init__(self, N):
        self.solutionSize = N
        self.first = Stack()
        self.second = Stack()
        self.third = Stack()
        for i in range(N, 0, -1):
            self.first.push(i)

    def solveTowers(self):
        self.moveDisk(self.solutionSize, self.first, self.second, self.third)

    def moveDisk(self, size, fr, helper, dest):
        if size == 1:
            data = fr.pop()
            dest.push(data)
        else:
            self.moveDisk(size - 1, fr, dest, helper)
            self.moveDisk(1, fr, helper, dest)
            self.moveDisk(size - 1, helper, fr, dest)

    def verifySolution(self):
        while not self.third.isEmpty():
            print self.third.pop()
