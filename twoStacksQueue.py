class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        self.stack1.append(value)

    # if empty, pop from stack1 and put each value in stack2.
    def dequeue(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        print(self.stack2.pop())

    # Print each of 2 stack's status
    def returnstackstage(self):
        print("Stack 1", self.stack1)
        print("Stack 2", self.stack2)


q = QueueUsingStacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
q.enqueue(40)
q.dequeue()
q.dequeue()
q.returnstackstage()