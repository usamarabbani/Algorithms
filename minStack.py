class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if not self.minStack:
            self.minStack.append(x)
        else:
            if x <= self.minStack[-1]:
                self.minStack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack:
            if self.minStack[-1] == self.stack[-1]:
                self.minStack.pop()
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.minStack:
            return self.minStack[-1]


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(4)
    minStack.push(5)
    minStack.push(1)
    minStack.push(3)
    assert minStack.getMin() == 1
    minStack.pop()
    minStack.pop()
    assert minStack.top() == 5
