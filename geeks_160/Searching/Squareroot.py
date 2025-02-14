'''
Given a positive integer n, find the square root of n. If n is not a perfect square, then return the floor value.

Floor value of any number is the greatest Integer which is less than or equal to that number

Examples:

Input: n = 4
Output: 2
Explanation: Since, 4 is a perfect square, so its square root is 2.
Input: n = 11
Output: 3
Explanation: Since, 11 is not a perfect square, floor of square root of 11 is 3.
Input: n = 1
Output: 1
Constraints:
1 ≤ n ≤  3 x 104
'''
#Complete this function
class Solution:
    def floorSqrt(self, n): 
        #Your code here
        left=0
        right=n
        while left<=right:
            mid=(left+right)//2
            if mid*mid>n:
                right=mid-1
            else:
                left=mid+1
        return left-1
    