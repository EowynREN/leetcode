class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.minStack = []

    def push(self, number):
        # write yout code here
        self.stack.append(number)
        if not self.minStack or number <= self.minStack[0]:
            self.minStack.append(number)

    def pop(self):
        # pop and return the top item in stack
        node = self.stack.pop()
        if self.minStack and node == self.minStack[0]:
            self.minStack.pop()
        return

    def min(self):
        # return the minimum number in stack
        return self.minStack[-1]
s = MinStack()
s.push(1)
s.pop()
s.push(2)
s.push(3)
s.min()
s.push(1)
s.min()