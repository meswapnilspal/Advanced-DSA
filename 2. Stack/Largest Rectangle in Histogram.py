"""
Q. Largest Rectangle in Histogram -

Given an array of integers A.
A represents a histogram i.e A[i] denotes the height of the ith histogram's bar. Width of each bar is 1.
Find the area of the largest rectangle formed by the histogram.

"""


class Solution:
	# @param A : list of integers
	# @return an integer
	def largestRectangleArea(self, A):
        def NSE(A,direction):
            n = len(A)
            stack = []
            ans = [None]*n

            if direction == "left":
                start = n-1
                end = -1
                hop = -1
                default_v = -1
            elif direction == "right":
                start = 0
                end = n
                hop = 1
                default_v = n

            for i in range(start,end,hop):
                while(len(stack) > 0 and A[i] < A[stack[-1]]):
                    ans[stack[-1]] = i
                    stack.pop()
                
                stack.append(i)
            
            for j in stack:
                ans[j] = default_v
            
            return ans
        
        n = len(A)
        maxarea = -1

        NSE_R = NSE(A,"right")
        NSE_L = NSE(A,"left")

        for i in range(n):
            right_bound = NSE_R[i]
            left_bound = NSE_L[i]

            Width = right_bound - left_bound - 1
            length = A[i]

            Area = Width * length

            maxarea = max(maxarea,Area)
        
        return maxarea