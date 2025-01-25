'''
Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

Note: Stock must be bought before being sold.

Examples:

Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
Output: 8
Explanation: You can buy the stock on day 2 at price = 1 and sell it on day 5 at price = 9. Hence, the profit is 8.
Input: prices[] = [7, 6, 4, 3, 1]
Output: 0 
Explanation: Here the prices are in decreasing order, hence if we buy any day then we cannot sell it at a greater price. Hence, the answer is 0.
Input: prices[] = [1, 3, 6, 9, 11]
Output: 10 
Explanation: Since the array is sorted in increasing order, we can make maximum profit by buying at price[0] and selling at price[n-1].
Constraint:
1 <= prices.size()<= 105
0 <= prices[i] <=104
'''
class Solution:
    def maximumProfit(self, prices):
        # code here
        i=0
        length=len(prices)
        max1=0
        min1=10**4
        bestTrans=0
        while i<length:
            if prices[i]<min1:
                min1=prices[i]
                max1=prices[i]
            else:
                max1=max(max1,prices[i])
                bestTrans=max(bestTrans,max1-min1)
            i+=1
        return bestTrans