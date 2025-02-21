'''
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
 

Constraints:

n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.
'''
from typing import List
#Using Cantor's Diagonal Argument
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        for i in range(len(nums)):
            curr = nums[i][i]
            ans.append("1" if curr == "0" else "0")
        
        return "".join(ans)

# class Solution:
#     def findDifferentBinaryString(self, nums: List[str]) -> str:
#         length=len(nums)
#         list1=[0]*(2**length)
#         for num in nums:
#             cur=int(num,2)
#             list1[cur]=1
#         val=list1.index(0)
#         return bin(val)[2:]
sol=Solution()
nums=["01","10"]
print(sol.findDifferentBinaryString(nums))