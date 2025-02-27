'''
A sequence x1, x2, ..., xn is Fibonacci-like if:

n >= 3
xi + xi+1 == xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

 

Example 1:

Input: arr = [1,2,3,4,5,6,7,8]
Output: 5
Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:

Input: arr = [1,3,7,11,12,14,18]
Output: 3
Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].
 

Constraints:

3 <= arr.length <= 1000
1 <= arr[i] < arr[i + 1] <= 109
'''

from functools import cache
from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        n = len(arr)
        max_len = 0

        dp = [[0] * n for _ in range(n)]


        val_to_idx = {num: idx for idx, num in enumerate(arr)}

        for curr in range(n):
            for prev in range(curr):

                diff = arr[curr] - arr[prev]
                prev_idx = val_to_idx.get(diff, -1)

                dp[prev][curr] = (
                    dp[prev_idx][prev] + 1
                    if diff < arr[prev] and prev_idx >= 0
                    else 2
                )
                max_len = max(max_len, dp[prev][curr])

        return max_len if max_len > 2 else 0
    
# more optimized

'''
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        fib_lens = {} # (a, b): length of subsequence
        set_arr = set(arr) # set of arrs for O(1) lookup

        for b, c in combinations(arr, 2):
            a = c - b # a + b = c
            if a < b and a in set_arr: # a < b since arr increasing, a found means (a, b, c) is fib
                # length of (b, c) = length of (a, b) + 1 for c. (a, b) is min 2
                fib_lens[(b, c)] = fib_lens.get((a, b), 2) + 1
                
        return max(fib_lens.values(), default = 0) # max length or 0 if no lengths
'''
    
sol=Solution()
arr=[1,2,3,4,5,6,7,8]
arr=[1,3,7,11,12,14,18]
arr=[2,4,7,8,9,10,14,15,18,23,32,50]
print(sol.lenLongestFibSubseq(arr))