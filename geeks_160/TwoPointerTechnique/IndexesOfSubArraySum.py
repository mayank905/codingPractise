'''
Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.

Note: If no such array is possible then, return [-1].

Examples:

Input: arr[] = [1, 2, 3, 7, 5], target = 12
Output: [2, 4]
Explanation: The sum of elements from 2nd to 4th position is 12.
Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15
Output: [1, 5]
Explanation: The sum of elements from 1st to 5th position is 15.
Input: arr[] = [5, 3, 4], target = 2
Output: [-1]
Explanation: There is no subarray with sum 2.
Constraints:
1 <= arr.size()<= 106
0 <= arr[i] <= 103
0 <= target <= 109
'''
class Solution:
    def subarraySum(self, arr, target):
        # code here
        sum1=0
        left=0
        right=0
        while right<len(arr):
            sum1+=arr[right]
            while left<right and sum1>target:
                sum1-=arr[left]
                left+=1
            if sum1==target:
                return [left+1,right+1]
            right+=1
        return [-1]

sol=Solution()
arr=[1, 2, 3, 7, 5]
target=12
arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target=15
# arr=[5, 3, 4]
# target=2
print(sol.subarraySum(arr,target))