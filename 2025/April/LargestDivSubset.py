'''
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.
'''
from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dict1=dict()
        def dp(index):
            if index==len(nums)-1:
                dict1[index]=[1,index,index]
                return dict1[index]
            curmax=(1,index,index)
            for i in range(index+1,len(nums)):
                if nums[i]%nums[index]!=0:
                    continue
                if i in dict1:
                    max1,index1,index2=dict1[i]
                else:
                    max1,index1,index2=dp(i)
                if max1+1>=curmax[0]:
                    curmax=[max1+1,index,index1]
            dict1[index]=curmax
            return curmax
        result=[]
        for i in range(len(nums)-1,-1,-1):
            dp(i)

        ind=max(dict1,key=lambda x:dict1[x][0])
        while dict1[ind][2]!=ind:
            result.append(nums[ind])
            ind=dict1[ind][2]
        result.append(nums[ind])
        return result
sol=Solution()
print(sol.largestDivisibleSubset([1,2,3])) # [1,2] or [1,3]
print(sol.largestDivisibleSubset([1,2,4,8])) # [1,2,4,8]
print(sol.largestDivisibleSubset([3,4,16,8])) # [4,8,16]
print(sol.largestDivisibleSubset([5,9,18,54,108,540,90,180,360,720])) # [9,18,90,180,360,720]