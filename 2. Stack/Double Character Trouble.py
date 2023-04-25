"""
Q. Double Character Trouble

You are given a string A.
An operation on the string is defined as follows:

Remove the first occurrence of the same consecutive characters. eg for a string "abbcd", the first occurrence of same consecutive characters is "bb".

Therefore the string after this operation will be "acd".
Keep performing this operation on the string until there are no more occurrences of the same consecutive characters and return the final string.

"""


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        s = list()
        n = len(A)
        for i in range(n):
            if len(s) == 0:
                s.append(A[i])
                continue

            if s[-1] == A[i]:
                s.pop()
            else:
                s.append(A[i])
        
        return (''.join(s))     