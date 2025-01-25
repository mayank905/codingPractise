from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        length=len(nums)
        count=0
        prev=nums[0]
        dict1=dict()
        index=0

        for i in range(1,length):
            if nums[i]>prev:
                prev=nums[i]
                count+=1
            else:
                dict1[index]=count+1
                index=i
                prev=nums[i]
                count=0
        dict1[index]=count+1
        maxk=0
        j=0
        while j<length-1:
            if j in dict1:
                val1=dict1[j]
                newIndex=j+val1
                if newIndex>length-1:
                    maxk=max(maxk,val1//2)
                    break
                val2=dict1[newIndex]
                min1=min(val1,val2)
                max1=max(val1,val2)
                if min1*2>=max1:
                    maxk=max(maxk,min1)
                else:
                    maxk=max(maxk,max1//2)
            j+=val1
        return maxk




 
        
sol=Solution()
nums = [2,5,7,8,9,2,3,4,3,1]
# nums = [5,8,-2,-1]
# nums = [-15,19]
# nums = [7,-14,-16,17,9,14]
print(sol.maxIncreasingSubarrays(nums))

'''
Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent 
subarrays
 of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:

Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return the maximum possible value of k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [2,5,7,8,9,2,3,4,3,1]

Output: 3

Explanation:

The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 3 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
Example 2:

Input: nums = [1,2,3,4,4,4,4,5,6,7]

Output: 2

Explanation:

The subarray starting at index 0 is [1, 2], which is strictly increasing.
The subarray starting at index 2 is [3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 2 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
 

Constraints:

2 <= nums.length <= 2 * 105
-109 <= nums[i] <= 109
'''