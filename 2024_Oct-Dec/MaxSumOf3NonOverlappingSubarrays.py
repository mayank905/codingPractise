'''
Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

 

Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] < 216
1 <= k <= floor(nums.length / 3)
'''
from collections import defaultdict
from functools import cache
from typing import List
import heapq


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        global prefixsum
        global pendingindex
        pendingindex=defaultdict(list)
        prefixsum=[0]*n
        prefixsum[0]=nums[0]
        for i in range(1,n):
            prefixsum[i]=prefixsum[i-1]+nums[i]
        @cache
        def miniprob(n,index,rl,rsub):
            global prefixsum
            global pendingindex
            if rsub:
                if rl==0:
                    return 0
                elif (rl//k)<rsub:
                    return 0
                else:
                    if index==0:
                        prev=0
                    else:
                        prev=prefixsum[index-1]
                    next1=prefixsum[index+k-1]
                    left=next1-prev+miniprob(n,index+k,rl-k,rsub-1)
                    right=miniprob(n,index+1,rl-1,rsub)
                    if left>=right:
                        heapq.heappush(pendingindex[left],index)
                        return left
                    else:
                        return right
            else:
                return 0

        max1=miniprob(n,0,n,3)
        result=[heapq.heappop(pendingindex[max1])]  
        remain=2
        prevtotal=max1 
        while remain:
            i=result[-1]
            nexttarget=prevtotal-(prefixsum[i+k-1] if i==0 else prefixsum[i+k-1]-prefixsum[i-1])
            if nexttarget in pendingindex and pendingindex[nexttarget]:
                temp=heapq.heappop(pendingindex[nexttarget])
                prevtotal=nexttarget
                result.append(temp)
                remain-=1                
            else:
                break
        return result

sol=Solution()
# nums=[1,2,1,2,6,7,5,1]
# k=2
nums=[7,13,20,19,19,2,10,1,1,19]
k=3
nums=[9,11,17,15,18,17,8,18,18,19,9,10,10,7,8,13,11,12,8,1]
k=2
print(sol.maxSumOfThreeSubarrays(nums,k))# [0,3,5]