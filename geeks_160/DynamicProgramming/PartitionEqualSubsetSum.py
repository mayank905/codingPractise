'''
Given an array arr[], determine if it can be partitioned into two subsets such that the sum of elements in both parts is the same.

Note: Each element must be in exactly one subset.

Examples:

Input: arr = [1, 5, 11, 5]
Output: true
Explanation: The two parts are [1, 5, 5] and [11].
Input: arr = [1, 3, 5]
Output: false
Explanation: This array can never be partitioned into two such parts.
Constraints:
1 ≤ arr.size ≤ 100
1 ≤ arr[i] ≤ 200
'''

class Solution:
    def equalPartition(self, arr):
        # code here
        sum1=sum(arr)
        if sum1%2:
            return False
        length=len(arr)
        target=sum1//2
        dp=[[False for _ in range(target+1)] for _ in range(length+1)]
        for i in range(length+1):
            dp[i][0]=True
        for i in range(1,length+1):
            for j in range(1,target+1):
                if arr[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
        return dp[length][target]