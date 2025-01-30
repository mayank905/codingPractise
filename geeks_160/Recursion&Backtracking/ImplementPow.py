'''Implement the function power(b, e), which calculates b raised to the power of e (i.e. be).

Examples:

Input: b = 3.00000, e = 5
Output: 243.00000
Input: b = 0.55000, e = 3
Output: 0.16638
Input: b = -0.67000, e = -7
Output: -16.49971
Constraints:

-100.0 < b < 100.0
-109 <= e <= 109
Either b is not zero or e > 0.
-104 <= be <= 104
'''
# Approach:


class Solution:
    def power(self, b: float, e: int) -> float:
        if e == 0:
            return 1
        if e < 0:
            return 1 / self.power(b, -e)
        if e % 2 == 0:
            return self.power(b * b, e // 2)
        return b * self.power(b, e - 1)