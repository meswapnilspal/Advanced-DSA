"""
Q. Sliding Window Maximum -

Given an array of integers A. There is a sliding window of size B, moving from the very left of the array to the very right. You can only see the B numbers in the window. Each time the sliding window moves rightwards by one position. You have to find the maximum for each window.

Return an array C, where C[i] is the maximum value in the array from A[i] to A[i+B-1].

Refer to the given example for clarity.

NOTE: If B > length of the array, return 1 element with the max of the array.

"""

from collections import deque
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def slidingMaximum(self, A, B):
        
        n = len(A)
        k = B
        
        if k == 1:
            return A
        elif k == n:
            return [max(A)]
        elif k > n:
            return 1

        dq = deque(maxlen=k)
        ans = []

        for i in range(k):
            while(len(dq) != 0 and A[i] > A[dq[-1]]):
                dq.pop() #remove back
            dq.append(i) #insert back
        
        ans.append(A[dq[0]]) #insert front element

        l = 1
        r = k

        while(r<n):
            if l-1 == dq[0]:
                dq.popleft() #popping since window shifted (expiring element)
            while(len(dq) != 0 and A[r] > A[dq[-1]]):
                dq.pop() #remove back
            dq.append(r) #insert back

            ans.append(A[dq[0]])
            l += 1
            r += 1
        
        return ans