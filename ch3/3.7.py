from SQDS import Queue

class Dog():

    def __init__(self, time):
        self.name = 'Dog'
        self.time = time
class Cat():

    def __init__(self, time):
        self.name = 'Cat'
        self.time = time

class AnimalShelter():

    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal):
        if animal.name == 'Cat':
            self.cats.enqueue(animal)
        elif animal.name == 'Dog':
            self.dogs.enqueue(animal)
        else:
            return 'Not an animal'

    def dequeueAny(self):
        if self.dogs.isEmpty() and self.cats.isEmpty():
            return 'Shelter is empty'
        if self.dogs.isEmpty():
            return self.cats.dequeue()
        elif self.cats.isEmpty():
            return self.dogs.dequeue()

        dog = self.dogs.peek()
        cat = self.cats.peek()

        if dog.time < cat.time:
            return self.dogs.dequeue()
        else:
            return self.cats.dequeue()

    def dequeueDog(self):
        if self.dogs.isEmpty():
            return 'There are no dogs'
        return self.dogs.dequeue()

    def dequeueCat(self):
        if self.cats.isEmpty():
            return ' There are no cats'
        return self.cats.dequeue()

