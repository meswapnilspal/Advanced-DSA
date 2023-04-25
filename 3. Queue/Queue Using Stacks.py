"""
Q. Queue Using Stacks -

Implement a First In First Out (FIFO) queue using stacks only.

The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the UserQueue class:

void push(int X) : Pushes element X to the back of the queue.
int pop() : Removes the element from the front of the queue and returns it.
int peek() : Returns the element at the front of the queue.
boolean empty() : Returns true if the queue is empty, false otherwise.
NOTES:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

"""

class UserQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        """
        Initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        """
        Push element x to the back of queue.
        """
        

    def pop(self) -> int:
        if len(self.s2) == 0:
            while self.s1:
                self.s2.append(self.s1.pop())
            popped = self.s2.pop()
        else:
            popped = self.s2.pop()
        
        return popped


        """
        Removes the element from in front of queue and returns that element.
        """
        

    def peek(self) -> int:
        if len(self.s2) == 0:
            front = self.s1[0]
        else:
            front = self.s2[-1]
        
        return front

        """
        Get the front element.
        """
        

    def empty(self) -> bool:
        if len(self.s1) == 0 and len(self.s2) == 0:
            return True
        else:
            return False
        """
        Returns whether the queue is empty.
        """

# Your UserQueue object will be instantiated and called as such:
# obj = UserQueue()
# obj.push(x)
# param2 = obj.pop()
# param3 = obj.peek()
# param4 = obj.empty()