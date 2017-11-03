class MyQueue(object):
    def __init__(self):
        self.inStack = []
        self.outStack = []
        self.size = 0
    
    # Rotate In / Out
    def rotate(self):
        if len(self.outStack) == 0:
            while len(self.inStack) > 0:
                self.outStack.append(self.inStack.pop())
        return 

    # Peek last
    def peek(self):
        if self.size == 0:
            return None

        self.rotate()
        return self.outStack[len(self.outStack) - 1]
    
    # Pop Last
    def pop(self):
        if self.size == 0:
            return None

        self.rotate()
        self.size -= 1
        return self.outStack.pop()
        
    # Put in inStack
    def put(self, value):
        self.size += 1
        self.inStack.append(value)
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
