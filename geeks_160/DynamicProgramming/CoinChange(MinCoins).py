'''
You are given an array coins[], where each element represents a coin of a different denomination, and a target value sum. You have an unlimited supply of each coin type {coins1, coins2, ..., coinsm}.

Your task is to determine the minimum number of coins needed to obtain the target sum. If it is not possible to form the sum using the given coins, return -1.

Examples:

Input: coins[] = [25, 10, 5], sum = 30
Output: 2
Explanation: Minimum 2 coins needed, 25 and 5  
Input: coins[] = [9, 6, 5, 1], sum = 19
Output: 3
Explanation: 19 = 9 + 9 + 1
Input: coins[] = [5, 1], sum = 0
Output: 0
Explanation: For 0 sum, we do not need a coin
Input: coins[] = [4, 6, 2], sum = 5
Output: -1
Explanation: Not possible to make the given sum.
 
Constraints:
1 ≤ sum * coins.size() ≤ 106
0 <= sum <= 104
1 <= coins[i] <= 104
1 <= coins.size() <= 103
'''
# class Solution:
#     def minCoins(self, coins, sum):
#     	# code here
#         dp=[10**6]*(sum+1)
#         coins.sort()
#         dp[0]=0
#         curmin=10**6
#         for coin in coins:
#             tsum=sum
#             tcoin=coin
#             i=1
#             while tsum>0:
#                 tsum-=tcoin
#                 if tcoin*i<sum+1:
#                     dp[tcoin*i]=min(i,dp[tcoin*i])
#                     i+=1
#         for coin in coins:
#             tsum=sum
#             tcoin=coin
#             i=1
#             if tsum%coin==0:
#                 curmin=min(curmin,tsum//coin)
#             while tsum>0:
#                 tsum-=tcoin
#                 if tsum>=0 and dp[tsum]!=10**6:
#                     curmin=min(curmin,(i+dp[tsum]))
#                 i+=1
#         return curmin if curmin!=10**6 else -1 
class Solution:
    def minCoins(self, coins, target_sum):
        # Create a dp array to store the minimum number of coins for each sum
        dp = [float('inf')] * (target_sum + 1)
        dp[0] = 0  # Base case: 0 coins are needed to make sum 0

        # Iterate over each coin
        for coin in coins:
            # Update dp array for all sums that can be achieved using the current coin
            for current_sum in range(coin, target_sum + 1):
                dp[current_sum] = min(dp[current_sum], 1 + dp[current_sum - coin])

        # If dp[target_sum] is still infinity, it means the target sum cannot be formed
        return dp[target_sum] if dp[target_sum] != float('inf') else -1
# Example usage
sol = Solution()
coins = [25, 10, 5]
sum = 30
print(sol.minCoins(coins, sum))  # Output: 2
coins = [9, 6, 5, 1]
sum = 19
print(sol.minCoins(coins, sum))  # Output: 3
coins = [5, 1]
sum = 0
print(sol.minCoins(coins, sum))  # Output: 0
coins = [4, 6, 2]
sum = 5
print(sol.minCoins(coins, sum))  # Output: -1
coins=[17, 3, 5, 18, 14]
sum=74
print(sol.minCoins(coins, sum))  # Output: 5
sum=3
coins=[1, 5, 9, 11, 15, 18]
print(sol.minCoins(coins, sum))  # Output: 1