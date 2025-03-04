'''
Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

 

Example 1:

Input: n = 12
Output: true
Explanation: 12 = 31 + 32
Example 2:

Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34
Example 3:

Input: n = 21
Output: false
 

Constraints:

1 <= n <= 107
'''

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        prev=15
        while n:
            i=0
            while 3**i<=n and i<prev:
                i+=1
            if 3**(i-1)==n:
                return True
            else:
                prev=i-1
                if prev==0:
                    return False
                n=n-(3**(i-1))
sol=Solution()
print(sol.checkPowersOfThree(21))