'''
Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.

Examples:

Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.
Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
Output: 5
Explanation: Only subarray with sum = 15 is [-5, 8, -14, 2, 4] of length 5.
Input: arr[] = [10, -10, 20, 30], k = 5
Output: 0
Explanation: No subarray with sum = 5 is present in arr[].
Constraints:
1 ≤ arr.size() ≤ 105
-104 ≤ arr[i] ≤ 104
-109 ≤ k ≤ 109
'''
class Solution:
    def longestSubarrayWithSumK(eslf,arr, k):
        n = len(arr)
        sum_dict = {}
        sum_dict[0] = -1
        max_len = 0
        sum = 0
        for i in range(n):
            sum += arr[i]
            if sum not in sum_dict:
                sum_dict[sum] = i
            if sum - k in sum_dict:
                max_len = max(max_len, i - sum_dict[sum - k])
        return max_len
sol=Solution()
arr=[10, 5, 2, 7, 1, -10]
k=15
print(sol.longestSubarrayWithSumK(arr,k)) #6