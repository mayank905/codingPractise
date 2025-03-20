'''
In daily share trading, a trader buys shares and sells them on the same day. If the trader is allowed to make at most 2 transactions in a day, find out the maximum profit that a share trader could have made.

You are given an array prices[] representing stock prices throughout the day. Note that the second transaction can only start after the first one is complete (buy->sell->buy->sell).

Examples:

Input: prices[] = [10, 22, 5, 75, 65, 80]
Output: 87
Explanation: 
Trader will buy at 10 and sells at 22. 
Profit earned in 1st transaction = 22 - 10 = 12. 
Then he buys at 5 and sell at 80. 
Profit earned in 2nd transaction = 80 - 5 = 75. 
Total profit earned = 12 + 75 = 87. 
Input: prices[] = [2, 30, 15, 10, 8, 25, 80]
Output: 100
Explanation: 
Trader will buy at 2 and sells at 30. 
Profit earned in 1st transaction = 30 - 2 = 28. 
Then he buys at 8 and sell at 80. 
Profit earned in 2nd transaction = 80 - 8 = 72. 
Total profit earned = 28 + 72 = 100.
Constraints:
1 <= prices.size() <= 105
1 <= prices[i] <= 105
'''
class Solution:
    def maxProfit(self, prices):
        # code here
        n=len(prices)
        if n==1:
            return 0
        dp=[[0]*n for _ in range(2)]
        for t in range(2):
            max_diff=-prices[0]
            for d in range(1,n):
                dp[t][d]=max(dp[t][d-1],prices[d]+max_diff)
                max_diff=max(max_diff,dp[t-1][d]-prices[d])
        return dp[1][n-1]
# Example usage
s = Solution()
prices = [10, 22, 5, 75, 65, 80]
print(s.maxProfit(prices)) # Output: 87