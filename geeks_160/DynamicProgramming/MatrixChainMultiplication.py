'''
Given an array arr[] which represents the dimensions of a sequence of matrices where the ith matrix has the dimensions (arr[i-1] x arr[i]) for i>=1, find the most efficient way to multiply these matrices together. The efficient way is the one that involves the least number of multiplications.

Examples:

Input: arr[] = [2, 1, 3, 4]
Output: 20
Explanation: There are 3 matrices of dimensions 2 × 1, 1 × 3, and 3 × 4, Let this 3 input matrices be M1, M2, and M3. There are two ways to multiply: ((M1 x M2) x M3) and (M1 x (M2 x M3)), note that the result of (M1 x M2) is a 2 x 3 matrix and result of (M2 x M3) is a 1 x 4 matrix. 
((M1 x M2) x M3)  requires (2 x 1 x 3) + (2 x 3 x 4) = 30 
(M1 x (M2 x M3))  requires (1 x 3 x 4) + (2 x 1 x 4) = 20. 
The minimum of these two is 20.
Input: arr[] = [1, 2, 3, 4, 3]
Output: 30
Explanation: There are 4 matrices of dimensions 1 × 2, 2 × 3, 3 × 4, 4 × 3. Let this 4 input matrices be M1, M2, M3 and M4. The minimum number of multiplications are obtained by ((M1 x M2) x M3) x M4). The minimum number is (1 x 2 x 3) + (1 x 3 x 4) + (1 x 4 x 3) = 30.
Input: arr[] = [3, 4]
Output: 0
Explanation: As there is only one matrix so, there is no cost of multiplication.
Constraints: 
2 ≤ arr.size() ≤ 100
1 ≤ arr[i] ≤ 200
'''
# Approach:
# The problem can be solved using dynamic programming. Let dp[i][j] be the minimum number of multiplications needed to multiply matrices from i to j. 
# The base case is when i == j, dp[i][j] = 0. The recursive relation is:
# dp[i][j] = min(dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]) for i <= k < j
# The answer will be dp[1][n - 1] where n is the size of the array.
class Solution:
    def matrixMultiplication(self, arr):
        # code here
        n = len(arr)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(1, n - 1):
            dp[i][i + 1] = arr[i - 1] * arr[i] * arr[i + 1]
        for gap in range(2, n):
            for i in range(1, n - gap):
                j = i + gap
                dp[i][j] = float('inf')
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j])
        return dp[1][n - 1]
# Time Complexity: O(n^3)
# Auxiliary Space: O(n^2)


sol=Solution()
print(sol.matrixMultiplication([2, 1, 3, 4])) #20
print(sol.matrixMultiplication([1, 2, 3, 4, 3])) #30
print(sol.matrixMultiplication([10,30,5,60])) #0
