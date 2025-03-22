'''
You are given an array arr[] which represents houses arranged in a circle, where each house has a certain value. A thief aims to maximize the total stolen value without robbing two adjacent houses.
Determine the maximum amount the thief can steal.

Note: Since the houses are in a circle, the first and last houses are also considered adjacent.

Examples:

Input: arr[] = [2, 3, 2]
Output: 3
Explanation: arr[0] and arr[2] can't be robbed because they are adjacent houses. Thus, 3 is the maximum value thief can rob.
Input: arr[] = [1, 2, 3, 1]
Output: 4
Explanation: Maximum stolen value: arr[0] + arr[2] = 1 + 3 = 4
Input: arr[] = [2, 2, 3, 1, 2]
Output: 5
Explanation: Maximum stolen value: arr[0] + arr[2] = 2 + 3 = 5 or arr[2] + arr[4] = 3 + 2 = 5
Constraints:
2 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 104
'''
# My solution:Time Limit exceeded after few cases
'''class Solution:
    def maxValue(self, arr):
        # code here
        dict1=dict()
        def dp(index,bol):
            if index>=len(arr):
                return 0
            if index==len(arr)-1:
                if bol:
                    return 0
            if (index,bol) in dict1:
                return dict1[(index,bol)]
            dict1[(index,bol)]=max(dp(index+1,bol),arr[index]+dp(index+2,bol))
            return dict1[(index,bol)]
        return max(dp(1,False),arr[0]+dp(2,True))'''
# Optimized solution
class Solution:
    def maxValue(self, arr):
        # code here
        length=len(arr)
        if length==1:
            return arr[0]
        if length==2:
            return max(arr[0],arr[1])
            
        def func(nums):
            prev1,prev2=0,0
            for num in nums:
                cur=max(prev2,prev1+num)
                prev1=prev2
                prev2=cur
            return prev2
        first=func(arr[1:])
        second=func(arr[:-1])
        return max(first,second)

sol=Solution()
arr=[2, 3, 2]
print(sol.maxValue(arr)) # Output: 3
arr=[1, 2, 3, 1]
print(sol.maxValue(arr)) # Output: 4
arr=[2, 2, 3, 1, 2]
print(sol.maxValue(arr)) # Output: 5