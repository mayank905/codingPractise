'''
You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. There exists another array, nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).

Return the bitwise XOR of all integers in nums3.

 

Example 1:

Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
Output: 13
Explanation:
A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
The bitwise XOR of all these numbers is 13, so we return 13.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 0
Explanation:
All possible pairs of bitwise XORs are nums1[0] ^ nums2[0], nums1[0] ^ nums2[1], nums1[1] ^ nums2[0],
and nums1[1] ^ nums2[1].
Thus, one possible nums3 array is [2,5,1,6].
2 ^ 5 ^ 1 ^ 6 = 0, so we return 0.
 

Constraints:

1 <= nums1.length, nums2.length <= 105
0 <= nums1[i], nums2[j] <= 109
'''
#Solution1

from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # Get lengths of arrays
        len1, len2 = len(nums1), len(nums2)

        # Dictionary to store frequency of each number
        freq = {}

        # Add frequencies for nums1 elements
        # Each element appears n2 times in final result
        for num in nums1:
            freq[num] = freq.get(num, 0) + len2

        # Add frequencies for nums2 elements
        # Each element appears n1 times in final result
        for num in nums2:
            freq[num] = freq.get(num, 0) + len1

        # XOR numbers that appear odd number of times
        ans = 0
        for num in freq:
            if freq[num] % 2:
                ans ^= num

        return ans
    
#Solution2

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # Initialize XOR results for both arrays
        xor1, xor2 = 0, 0

        # Get lengths of both arrays
        len1, len2 = len(nums1), len(nums2)

        # If nums2 length is odd, each element in nums1 appears odd times in final result
        if len2 % 2:
            for num in nums1:
                xor1 ^= num

        # If nums1 length is odd, each element in nums2 appears odd times in final result
        if len1 % 2:
            for num in nums2:
                xor2 ^= num

        # Return XOR of both results
        return xor1 ^ xor2
    
#Solution3

from functools import reduce
from operator import xor

class Solution:
    def xorAllNums(self, A, B):
        return (len(A) % 2 * reduce(xor, B)) ^ (len(B) % 2 * reduce(xor, A))