class MyQueue:

    def __init__(self):
        self.st1=[]
        self.st2=[]

    def push(self, x):
        self.st1.append(x)

    def pop(self):
        while self.st1:
            self.st2.append( self.st1.pop() )

        x=self.st2.pop()

        while self.st2:
            self.st1.append( self.st2.pop() )
        return x

    def peek(self):
        while self.st1:
            self.st2.append(self.st1.pop())
        x=self.st2[-1]

        while self.st2:
            self.st1.append( self.st2.pop() )
        return x

    def empty(self):
        return not (self.st1 or self.st2)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()