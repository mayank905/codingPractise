'''
In the stock market, a person buys a stock and sells it on some future date. You are given an array prices[] representing stock prices on different days and a positive integer k, find out the maximum profit a person can make in at-most k transactions.

A transaction consists of buying and subsequently selling a stock and new transaction can start only when the previous transaction has been completed.

Examples :

Input: prices[] = [10, 22, 5, 80], k = 2
Output: 87
Explaination:
1st transaction: Buy at 10 and sell at 22. 
2nd transaction : Buy at 5 and sell at 80.
Total Profit will be 12 + 75 = 87.
Input: prices[] = [20, 580, 420, 900], k = 3
Output: 1040
Explaination: 
1st transaction: Buy at 20 and sell at 580. 
2nd transaction : Buy at 420 and sell at 900.
Total Profit will be 560 + 480 = 1040.
Input: prices[] = [100, 90, 80, 50, 25],  k = 1
Output: 0
Explaination: Selling price is decreasing continuously
leading to loss. So seller cannot have any profit.
Constraints:
1 ≤ prices.size() ≤ 103
1 ≤ k ≤ 200
1 ≤ prices[i] ≤ 103
'''

class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        # If k is greater than n // 2, it's equivalent to unlimited transactions
        if k >= n // 2:
            return self.maxProfitUnlimited(prices)

        # DP table to store the maximum profit
        dp = [[0] * n for _ in range(k + 1)]

        # Fill the DP table
        for t in range(1, k + 1):   
            max_diff = -prices[0]
            for d in range(1, n):
                dp[t][d] = max(dp[t][d - 1], prices[d] + max_diff)
                max_diff = max(max_diff, dp[t - 1][d] - prices[d])

        return dp[k][n - 1]

    def maxProfitUnlimited(self, prices):
        # Helper function to calculate max profit with unlimited transactions
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

# Example usage
sol = Solution()
prices = [10, 22, 5, 80,60,70]
k = 2
print(sol.maxProfit(k, prices))  # Output: 87

# prices = [20, 580, 420, 900]
# k = 3
# print(sol.maxProfit(k, prices))  # Output: 1040

# prices = [100, 90, 80, 50, 25]
# k = 1
# print(sol.maxProfit(k, prices))  # Output: 0