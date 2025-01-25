'''
Given an array arr of 0s and 1s. Find and return the length of the longest subarray with equal number of 0s and 1s.

Examples:

Input: arr[] = [1, 0, 1, 1, 1, 0, 0]
Output: 6
Explanation: arr[1...6] is the longest subarray with three 0s and three 1s.
Input: arr[] = [0, 0, 1, 1, 0]
Output: 4
Explnation: arr[0...3] or arr[1...4] is the longest subarray with two 0s and two 1s.
Input: arr[] = [0]
Output: 0
Explnation: There is no subarray with an equal number of 0s and 1s.
Constraints:
1 <= arr.size() <= 105
0 <= arr[i] <= 1
'''
class Solution:
    def longestSubarrayOf0and1(self,arr):
        n = len(arr)
        sum_dict = {}
        sum_dict[0] = -1
        max_len = 0
        sum = 0
        for i in range(n):
            sum += 1 if arr[i] == 1 else -1
            if sum not in sum_dict:
                sum_dict[sum] = i
            else:
                max_len = max(max_len, i - sum_dict[sum])
        return max_len
sol=Solution()
arr=[1, 0, 1, 1, 1, 0, 0]
print(sol.longestSubarrayOf0and1(arr)) #6