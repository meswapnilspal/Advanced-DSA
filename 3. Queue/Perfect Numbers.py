"""
Q. Perfect Numbers -

Given an integer A, you have to find the Ath Perfect Number.

A Perfect Number has the following properties:

It comprises only 1 and 2.

The number of digits in a Perfect number is even.

It is a palindrome number.

For example, 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not.

"""


from queue import Queue
class Solution:
    # @param A : integer
    # @return a strings    
    def solve(self, A):   
        pn = Queue()
        pn.put("1")
        pn.put("2")

        c = 0
        while(c<A):
            front = pn.get()
            c +=1
            if c == A:
                return (front + front[::-1])
            v1 = front + "1"
            v2 = front + "2"
            # v1 = v1 + v1[::-1]
            # v2 = v2 + v2[::-1]
            pn.put(v1)
            pn.put(v2)