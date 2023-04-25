"""
Q. Min Stack -

Design a stack that supports push, pop, top, and retrieve the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
NOTE:
All the operations have to be constant time operations.
getMin() should return -1 if the stack is empty.
pop() should return nothing if the stack is empty.
top() should return -1 if the stack is empty.

"""


import math
class MinStack:
   
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)
        if x < self.min_stack[-1]:
            self.min_stack.append(x)
        # self.maintain_min = min(self.maintain_min,x)                

    # @return nothing
    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()
    
    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]
        return -1
        

    # @return an integer
    def getMin(self):
        if self.min_stack[-1] == math.inf:
            return -1
        return self.min_stack[-1]
    
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]