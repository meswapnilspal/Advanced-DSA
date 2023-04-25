"""
Q. Nearest Smaller Element -


Given an array A, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

More formally,

G[i] for an element A[i] = an element A[j] such that

j is maximum possible AND

j < i AND

A[j] < A[i]

Elements for which no smaller element exist, consider the next smaller element as -1.

"""


class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
        n = len(A)
        stack = []
        ans = [None]*n

        for i in range(n-1,-1,-1):
            while(len(stack) > 0 and A[i] < A[stack[-1]]):
                ans[stack[-1]] = A[i]
                stack.pop()
            
            stack.append(i)
        
        for j in stack:
            ans[j] = -1
        
        return ans