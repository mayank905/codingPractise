from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        length=len(arr)
        left=0
        right=length-1
        leftchange=True
        rightchange=True
        for i in range(1,length):
            if leftchange and arr[i]>=arr[left]:
                left=i
            else:
                leftchange=False
            if rightchange and arr[length-1-i]<=arr[right]:
                right=length-1-i
            else:
                rightchange=False
        if left==length-1 and right==0:
            return 0
        length1=left
        length2=right
        while length1>=0:
            if arr[length1]>arr[right]:
                length1-=1
            else:
                break
        while length2<=length-1:
            if arr[length2]<arr[left]:
                length2+=1
            else:
                break
        left1=left
        right1=right

        while left1>=0 and right1<=length-1:
            if arr[left1]>arr[right1]:
                left1-=1
                if arr[left1]!=arr[right1]:
                    right1+=1
            else:
                break

        return min(right-length1-1,length2-left-1,right1-left1-1,right1-left1-1)
    
sol=Solution()
arr=[1,2,3,10,4,2,3,5]
# arr=[5,4,3,2,1]
# arr=[1,2,3]
# arr=[1,2,3,10,0,7,8,9]
arr=[1,2,3,10,0,2,7,8,9]
print(sol.findLengthOfShortestSubarray(arr))

'''
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
Example 2:

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
Example 3:

Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.
 

Constraints:

1 <= arr.length <= 105
0 <= arr[i] <= 109

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        right = len(arr) - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        ans = right
        left = 0
        while left < right and (left == 0 or arr[left - 1] <= arr[left]):
            # find next valid number after arr[left]
            while right < len(arr) and arr[left] > arr[right]:
                right += 1
            # save length of removed subarray
            ans = min(ans, right - left - 1)
            left += 1
        return ans
'''