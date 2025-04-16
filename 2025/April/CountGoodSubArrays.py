'''
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.
Example 2:

Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i], k <= 109
'''
from collections import defaultdict
from typing import List
#optimize solution
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n=len(nums)
        freq=defaultdict(int)
        ans, cnt, l=0, 0, 0
        for r,x in enumerate(nums):
            cnt+=freq[x]
            freq[x]+=1
            while cnt>=k:
                ans+=n-r
                freq[nums[l]]-=1
                cnt-=freq[nums[l]]
                l+=1
        return ans

sol=Solution()
print(sol.countGood([1,1,1,1,1],10)) # 1
print(sol.countGood([3,1,4,3,2,2,4],2)) # 4
print(sol.countGood([2,3,3,3,3,1,3,1,3,2],19)) # 0
print(sol.countGood([2,1,3,1,2,2,3,3,2,2,1,1,1,3,1],11)) # 0