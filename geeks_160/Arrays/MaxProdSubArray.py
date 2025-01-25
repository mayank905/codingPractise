'''
Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

Note: It is guaranteed that the output fits in a 32-bit integer.

Examples

Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is {6, -3, -10} with product = 6 * (-3) * (-10) = 180.
Input: arr[] = [-1, -3, -10, 0, 6]
Output: 30
Explanation: The subarray with maximum product is {-3, -10} with product = (-3) * (-10) = 30.
Input: arr[] = [2, 3, 4] 
Output: 24 
Explanation: For an array with all positive elements, the result is product of all elements. 
Constraints:
1 ≤ arr.size() ≤ 106
-10  ≤  arr[i]  ≤  10
'''
class Solution:
    def maxProduct(self, arr):
        n = len(arr)
        if n==1:
            return arr[0]

        max_ending = 0
        min_ending = 0
        max_so_far = 0
        for i in range(n):

            if arr[i] < 0:
                temp = max_ending
                max_ending = min_ending
                min_ending = temp

            max_ending = max(arr[i], max_ending * arr[i])
            min_ending = min(arr[i], min_ending * arr[i])
            max_so_far = max(max_so_far, max_ending)
        return max_so_far
                
