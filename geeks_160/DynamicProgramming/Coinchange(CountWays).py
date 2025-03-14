'''
Given an integer array coins[ ] representing different denominations of currency and an integer sum, find the number of ways you can make sum by using different combinations from coins[ ]. 
Note: Assume that you have an infinite supply of each type of coin. Therefore, you can use any coin as many times as you want.
Answers are guaranteed to fit into a 32-bit integer. 

Examples:

Input: coins[] = [1, 2, 3], sum = 4
Output: 4
Explanation: Four Possible ways are: [1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3].
Input: coins[] = [2, 5, 3, 6], sum = 10
Output: 5
Explanation: Five Possible ways are: [2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 2, 6], [2, 3, 5] and [5, 5].
Input: coins[] = [5, 10], sum = 3
Output: 0
Explanation: Since all coin denominations are greater than sum, no combination can make the target sum.
Constraints:
1 <= sum <= 103
1 <= coins[i] <= 104
1 <= coins.size() <= 103
'''
#Top-Down Approach
'''class Solution:
    def count(self, coins, sum):
        # code here
        global set1
        set1=dict()
        def dp(cursum,index):
            if cursum==0:
                return 1
            if cursum<0:
                return 0
            if index>=len(coins):
                return 0
            if (cursum,index) in set1:
                return set1[(cursum,index)]
            left=dp(cursum-coins[index],index)
            right=dp(cursum,index+1)
            set1[(cursum,index)]=left+right
            return left+right
        return dp(sum,0)'''
#Top-Down Approach
class Solution:
    def count(self, coins, target_sum):
        # Create a dp array to store the number of ways to make each sum
        dp = [0] * (target_sum + 1)
        dp[0] = 1  # Base case: There's one way to make sum 0 (by using no coins)

        # Iterate over each coin
        for coin in coins:
            # Update dp array for all sums that can be achieved using the current coin
            for current_sum in range(coin, target_sum + 1):
                dp[current_sum] += dp[current_sum - coin]

        return dp[target_sum]
sol=Solution()
coins=[1, 2, 3]
sum=4
print(sol.count(coins, sum))  # Output: 4
coins=[2, 5, 3, 6]
sum=10
print(sol.count(coins, sum))  # Output: 5
coins=[5, 10]
sum=3
print(sol.count(coins, sum))  # Output: 0