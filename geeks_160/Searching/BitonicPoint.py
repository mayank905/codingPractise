'''
Given an array of integers arr[] that is first strictly increasing and then maybe strictly decreasing, find the bitonic point, that is the maximum element in the array.
Bitonic Point is a point before which elements are strictly increasing and after which elements are strictly decreasing.

Examples:

Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
Output: 8
Explanation: Elements before 8 are strictly increasing [1, 2, 4, 5, 7] and elements after 8 are strictly decreasing [3].
Input: arr[] = [10, 20, 30, 40, 50]
Output: 50
Explanation: Elements before 50 are strictly increasing [10, 20, 30 40] and there are no elements after 50.
Input: arr[] = [120, 100, 80, 20, 0]
Output: 120
Explanation: There are no elements before 120 and elements after 120 are strictly decreasing [100, 80, 20, 0].
Constraints:
3 ≤ arr.size() ≤ 105
1 ≤ arr[i]≤ 106
'''
class Solution:

    def findMaximum(self, arr):
        # code here
        left=0
        length=len(arr)
        right=length-1
        if arr[-1]<arr[0]>arr[1]:
             return arr[0]
        while left<=right:
            mid=(left+right)//2
            l=(mid-1)
            r=(mid+1)
            if arr[l]<arr[mid]<arr[r]:
                left=mid+1
            elif arr[l]>arr[mid]>arr[r]:
                right=mid-1
            else:
	            return arr[mid]
sol=Solution()
arr=[1, 2, 4, 5, 7, 8, 3]
print(sol.findMaximum(arr))