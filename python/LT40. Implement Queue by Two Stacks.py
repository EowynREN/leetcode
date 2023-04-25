class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, element):
        # write your code here
        self.stack1.append(element)

    def top(self):
        # write your code here
        # return the top element
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())

        top = self.stack1[0]
        self.stack2.append(self.stack1.pop())

        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return top

    def pop(self):
        # write your code here
        # pop and return the top element
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())

        top = self.stack1.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return top

m = MyQueue()
m.push(1)
m.pop()
m.push(2)
m.push(3)
m.top()
m.pop()