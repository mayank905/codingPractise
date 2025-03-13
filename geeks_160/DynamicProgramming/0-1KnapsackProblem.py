'''
Given n items, each with a specific weight and value, and a knapsack with a capacity of W, the task is to put the items in the knapsack such that the sum of weights of the items <= W and the sum of values associated with them is maximized. 

Note: You can either place an item entirely in the bag or leave it out entirely. Also, each item is available in single quantity.

Examples :

Input: W = 4, val[] = [1, 2, 3], wt[] = [4, 5, 1] 
Output: 3
Explanation: Choose the last item, which weighs 1 unit and has a value of 3.
Input: W = 3, val[] = [1, 2, 3], wt[] = [4, 5, 6] 
Output: 0
Explanation: Every item has a weight exceeding the knapsack's capacity (3).
Input: W = 5, val[] = [10, 40, 30, 50], wt[] = [5, 4, 2, 3] 
Output: 80
Explanation: Choose the third item (value 30, weight 2) and the last item (value 50, weight 3) for a total value of 80.
Constraints:
2 ≤ val.size() = wt.size() ≤ 103
1 ≤ W ≤ 103
1 ≤ val[i] ≤ 103
1 ≤ wt[i] ≤ 103
'''

# class Solution:
#     def knapsack(self, W, val, wt):
#         # Memoization dictionary to store the results of subproblems
#         memo = {}

#         def dp(index, curwt):
#             # If the subproblem has already been solved, return the result
#             if (index, curwt) in memo:
#                 return memo[(index, curwt)]
            
#             # Base case: if we have considered all items or the current weight exceeds the capacity
#             if index == len(val) or curwt > W:
#                 return 0
            
#             # If the current weight exceeds the capacity, skip the current item
#             if curwt + wt[index] > W:
#                 result = dp(index + 1, curwt)
#             else:
#                 # Consider both including and excluding the current item
#                 include = val[index] + dp(index + 1, curwt + wt[index])
#                 exclude = dp(index + 1, curwt)
#                 result = max(include, exclude)
            
#             # Store the result in the memoization dictionary
#             memo[(index, curwt)] = result
#             return result

#         return dp(0, 0)
    
class Solution:
    def knapsack(self, W, val, wt):
        n = len(val)
        # Create a 2D array to store the maximum value that can be obtained
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

        # Fill the dp array
        for i in range(1, n + 1):
            for w in range(1, W + 1):
                if wt[i - 1] <= w:
                    dp[i][w] = max(dp[i - 1][w], val[i - 1] + dp[i - 1][w - wt[i - 1]])
                else:
                    dp[i][w] = dp[i - 1][w]

        return dp[n][W]

# Example usage
sol = Solution()
W = 4
val = [1, 2, 3]
wt = [4, 5, 1]
print(sol.knapsack(W, val, wt))  # Output: 3

W = 3
val = [1, 2, 3]
wt = [4, 5, 6]
print(sol.knapsack(W, val, wt))  # Output: 0

W = 5
val = [10, 40, 30, 50]
wt = [5, 4, 2, 3]
print(sol.knapsack(W, val, wt))  # Output: 80

W = 50
val = [60, 100, 120]
wt = [10, 20, 30]
print(sol.knapsack(W, val, wt))  # Output: 220

W = 30
val = [60, 100, 120]
wt = [10, 20, 30]
print(sol.knapsack(W, val, wt))  # Output: 160