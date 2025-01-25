

'''
You are given an integer array nums. A good 
subsequence
 is defined as a subsequence of nums where the absolute difference between any two consecutive elements in the subsequence is exactly 1.

Return the sum of all possible good subsequences of nums.

Since the answer may be very large, return it modulo 109 + 7.

Note that a subsequence of size 1 is considered good by definition.

 

Example 1:

Input: nums = [1,2,1]

Output: 14

Explanation:

Good subsequences are: [1], [2], [1], [1,2], [2,1], [1,2,1].
The sum of elements in these subsequences is 14.
Example 2:

Input: nums = [3,4,5]

Output: 40

Explanation:

Good subsequences are: [3], [4], [5], [3,4], [4,5], [3,4,5].
The sum of elements in these subsequences is 40.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
mod = 10 ** 9 + 7

class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        dp = Counter()
        cnt = Counter()
        
        for num in nums:
            v1 = (dp[num - 1] + dp[num + 1] + (cnt[num - 1] + cnt[num + 1] + 1) * num % mod) % mod
            v2 = (cnt[num - 1] + cnt[num + 1] + 1) % mod
            dp[num] += v1
            dp[num] %= mod
            cnt[num] += v2
            cnt[num] %= mod
        
        return sum(dp.values()) % mod
'''