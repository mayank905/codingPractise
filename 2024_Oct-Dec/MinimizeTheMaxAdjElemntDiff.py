from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)

        big = 0
        small = 10 ** 9
        ones = []
        twos = []
        now = 0
        
        left = -1
        count = 0
        pre = -1
        for idx, num in enumerate(nums):
            if num == -1:
                if count > 0:
                    count += 1
                else:
                    left = pre
                    if left != -1:
                        big = max(big, left)
                        small = min(small, left)
                    count = 1
            else:
                if count == 0:
                    if pre != -1:
                        now = max(now, abs(pre - num))
                else:
                    big = max(big, num)
                    small = min(small, num)
                    if left != -1:
                        if count == 1:
                            ones.append((left, num))
                        else:
                            twos.append((left, num))
                    count = 0
            pre = num
        
        def helper(diff):
            num1 = small + diff
            num2 = big - diff
            if num1 >= num2:
                return True
            flag = (num2 - num1) <= diff
            for left, right in ones:
                if abs(left - num1) <= diff and abs(right - num1) <= diff:
                    continue
                if abs(left - num2) <= diff and abs(right - num2) <= diff:
                    continue
                return False
            for left, right in twos:
                if abs(left - num1) <= diff and abs(right - num1) <= diff:
                    continue
                if abs(left - num2) <= diff and abs(right - num2) <= diff:
                    continue
                if flag:
                    continue
                return False
            return True
                
        left = now
        right = max(big - small, now)
        while left < right:
            mid = (left + right) >> 1
            if helper(mid):
                right = mid
            else:
                left = mid + 1
        return left
sol=Solution()
nums = [[1,2,-1,10,8],
[-1,-1,-1],
[-1,10,-1,8]]
for num in nums:
    print(sol.minDifference(num))
    
'''
You are given an array of integers nums. Some values in nums are missing and are denoted by -1.

You can choose a pair of positive integers (x, y) exactly once and replace each missing element with either x or y.

You need to minimize the maximum absolute difference between adjacent elements of nums after replacements.

Return the minimum possible difference.

 

Example 1:

Input: nums = [1,2,-1,10,8]

Output: 4

Explanation:

By choosing the pair as (6, 7), nums can be changed to [1, 2, 6, 10, 8].

The absolute differences between adjacent elements are:

|1 - 2| == 1
|2 - 6| == 4
|6 - 10| == 4
|10 - 8| == 2
Example 2:

Input: nums = [-1,-1,-1]

Output: 0

Explanation:

By choosing the pair as (4, 4), nums can be changed to [4, 4, 4].

Example 3:

Input: nums = [-1,10,-1,8]

Output: 1

Explanation:

By choosing the pair as (11, 9), nums can be changed to [11, 10, 9, 8].

 

Constraints:

2 <= nums.length <= 105
nums[i] is either -1 or in the range [1, 109].
'''