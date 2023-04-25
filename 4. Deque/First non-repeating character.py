"""
Q. First non-repeating character -

Given a string A denoting a stream of lowercase alphabets, you have to make a new string B.
B is formed such that we have to find the first non-repeating character each time a character is inserted to the stream and append it at the end to B. If no non-repeating character is found, append '#' at the end of B.

"""

from collections import deque
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = len(A)
        hm_freq = dict()
        dq = deque([])
        ans = []

        for i in range(n):
            #adding to hashmap
            ele = A[i]
            if ele in hm_freq:
                hm_freq[ele] += 1
            else:
                hm_freq[ele] = 1
            
            #add to deque
            dq.append(ele)

            #adding to ans after looking it up in hashmap
            ans_char = ""
            while(len(dq) != 0):
                front = dq[0]
                if hm_freq[front] > 1:
                    dq.popleft()
                elif hm_freq[front] == 1:
                    ans_char = front
                    break
            
            if len(dq) == 0:
                ans_char = "#"
            
            ans.append(ans_char)
        
        ans_str = ''.join([str(elem) for elem in ans])
        return ans_str