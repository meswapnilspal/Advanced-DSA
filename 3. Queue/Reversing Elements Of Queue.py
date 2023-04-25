"""

Q. Reversing Elements Of Queue -

Given an array of integers A and an integer B, we need to reverse the order of the first B elements of the array, leaving the other elements in the same relative order.

NOTE: You are required to the first insert elements into an auxiliary queue then perform Reversal of first B elements.

"""

# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return a list of integers
#     def solve(self, A, B):


from queue import Queue
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        reversing_list = Queue()
        idx = B-1
        for i in range(idx, -1, -1):
            reversing_list.put(A[i])

        for i in range(idx+1,n):
            reversing_list.put(A[i])
        
        ans = []
        for i in range(n):
            tmp = reversing_list.get()
            ans.append(tmp)
        
        return ans