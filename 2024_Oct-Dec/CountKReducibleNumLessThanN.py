

'''
You are given a binary string s representing a number n in its binary form.

You are also given an integer k.

An integer x is called k-reducible if performing the following operation at most k times reduces it to 1:

Replace x with the count of 
set bits
 in its binary representation.
For example, the binary representation of 6 is "110". Applying the operation once reduces it to 2 (since "110" has two set bits). Applying the operation again to 2 (binary "10") reduces it to 1 (since "10" has one set bit).

Return an integer denoting the number of positive integers less than n that are k-reducible.

Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: s = "111", k = 1

Output: 3

Explanation:

n = 7. The 1-reducible integers less than 7 are 1, 2, and 4.

Example 2:

Input: s = "1000", k = 2

Output: 6

Explanation:

n = 8. The 2-reducible integers less than 8 are 1, 2, 3, 4, 5, and 6.

Example 3:

Input: s = "1", k = 3

Output: 0

Explanation:

There are no positive integers less than n = 1, so the answer is 0.

 

Constraints:

1 <= s.length <= 800
s has no leading zeros.
s consists only of the characters '0' and '1'.
1 <= k <= 5
mod = 10 ** 9 + 7

pre = [0] * 1001
for i in range(2, 1001):
    pre[i] = pre[i.bit_count()] + 1

class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        s = [int(x) for x in s]
        
        n = len(s)
        dp = [0] * (n + 1)
        
        cur = 0
        for i in range(n):
            for j in range(i - 1, -1, -1):
                    dp[j + 1] += dp[j]
                    dp[j] %= mod
            if s[i]:
                dp[cur] += 1
                dp[cur] %= mod
            cur += s[i]
        
        ans = 0
        for i in range(n + 1):
            if pre[i] < k:
                ans += dp[i]
        return (ans - 1) % mod
'''