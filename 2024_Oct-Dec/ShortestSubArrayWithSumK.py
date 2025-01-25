from collections import deque
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], target_sum: int) -> int:
        n = len(nums)

        # Size is n+1 to handle subarrays starting from index 0
        prefix_sums = [0] * (n + 1)

        # Calculate prefix sums
        for i in range(1, n + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

        candidate_indices = deque()

        shortest_subarray_length = float("inf")

        for i in range(n + 1):
            # Remove candidates from front of deque where subarray sum meets target
            while (
                candidate_indices
                and prefix_sums[i] - prefix_sums[candidate_indices[0]]
                >= target_sum
            ):
                # Update shortest subarray length
                shortest_subarray_length = min(
                    shortest_subarray_length, i - candidate_indices.popleft()
                )

            # Maintain monotonicity by removing indices with larger prefix sums
            while (
                candidate_indices
                and prefix_sums[i] <= prefix_sums[candidate_indices[-1]]
            ):
                candidate_indices.pop()

            # Add current index to candidates
            candidate_indices.append(i)

        # Return -1 if no valid subarray found
        return (
            shortest_subarray_length
            if shortest_subarray_length != float("inf")
            else -1
        )
#FAiled Solution

# class Solution:
#     def shortestSubarray(self, nums: List[int], k: int) -> int:
#         length=len(nums)
#         def isValid(gap):
#             for i in range(gap-1,length):
#                 if i-gap<0:
#                     prev=0
#                 else:
#                     prev=prefixarr[i-gap]
#                 if prefixarr[i]-prev>=k:
#                     return True
#             return False
#         prev=nums[0]
#         prefixarr=[]
#         prefixarr.append(prev)
#         for i in range(1,length):
#             prev+=nums[i]
#             prefixarr.append(prev)

#         left=1
#         right=len(nums)
#         result=-1
#         while left<=right:
#             mid=left+(right-left)//2
#             if isValid(mid):
#                 result=mid
#                 right=mid-1
#             else:
#                 left=mid+1
#         return result
sol=Solution()
nums = [
    # ([1],1),
    #     ([1,2],4),
    #     ([2,-1,2],3),
        ([44,-25,75,-50,-38,-42,-32,-6,-40,-47],19)] 
for num,k in nums:

    print(sol.shortestSubarray(num,k))

'''
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
1 <= k <= 109
'''