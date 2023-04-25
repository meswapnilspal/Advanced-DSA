"""
Q. First non-repeating character -

Given a string A denoting a stream of lowercase alphabets, you have to make a new string B.
B is formed such that we have to find the first non-repeating character each time a character is inserted to the stream and append it at the end to B. If no non-repeating character is found, append '#' at the end of B.

"""

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        def enqueue(q,ele):
            q.append(ele)
        
        def dequeue(q):
            q.pop(0)
        
        def getfront(q):
            if len(q) == 0:
                return "#"
            return q[0]
        
        def getrear(q):
            return q[-1]
        
        hm = dict()
        queue = []
        # ans = A[0]
        ans = ""
        
        n = len(A)
        for i in range(n):
            ele = A[i]
            if ele in hm:
                hm[ele] += 1
            else:
                hm[ele] = 1
            
            enqueue(queue,ele)

            front = getfront(queue)
            if front == "#":
                ans = ans + "#"
            else:
                while len(queue) > 0 and hm[front] > 1:
                    dequeue(queue)
                    front = getfront(queue)
                if len(queue) == 0:
                    ans = ans + "#"
                else:
                    ans = ans + front
        return ans