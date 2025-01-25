'''
Given an unsorted array of integers, find the number of continuous subarrays having sum exactly equal to a given number k.

Examples:

Input: arr = [10, 2, -2, -20, 10], k = -10
Output: 3
Explaination: Subarrays: arr[0...3], arr[1...4], arr[3...4] have sum exactly equal to -10.
Input: arr = [9, 4, 20, 3, 10, 5], k = 33
Output: 2
Explaination: Subarrays: arr[0...2], arr[2...4] have sum exactly equal to 33.
Input: arr = [1, 3, 5], k = 0
Output: 0
Explaination: No subarray with 0 sum.
Constraints:

1 ≤ arr.size() ≤ 105
-103 ≤ arr[i] ≤ 103
-107 ≤ k ≤ 107
'''
class Solution:
    def countSubarrays(self, arr, k):
        # code here
        length=len(arr)
        dict1=dict()
        dict1[0]=1
        count=0
        sum1=0
        for i in range(length):
            sum1+=arr[i]
            if (sum1-k) in dict1:
                count+=dict1[sum1-k]
            dict1[sum1]=dict1.get(sum1,0)+1
        return count
sol=Solution()
arr = [10, 2, -2, -20, 10]
k = -10
print(sol.countSubarrays(arr,k)) #3