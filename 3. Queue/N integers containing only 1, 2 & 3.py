"""
Q. N integers containing only 1, 2 & 3 -
Given an integer, A. Find and Return first positive A integers in ascending order containing only digits 1, 2, and 3.

NOTE: All the A integers will fit in 32-bit integers.

"""

from queue import Queue
class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        pn3 = Queue()
        c = 0
        ans = []
        while(c<A):
            if pn3.empty():
                front = ""
            else:
                front = pn3.get()
            
            v1 = int(str(front) + "1")
            pn3.put(v1)
            ans.append(v1)
            c += 1
            if c == A:
                return ans

            v2 = int(str(front) + "2")
            pn3.put(v2)
            ans.append(v2)
            c += 1
            if c == A:
                return ans

            v3 = int(str(front) + "3")
            pn3.put(v3)
            ans.append(v3)
            c += 1
            if c == A:
                return ans