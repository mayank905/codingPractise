'''
Given an array of integers cost[] where cost[i] is the cost of the ith step on a staircase. Once the cost is paid, you can either climb one or two steps. Return the minimum cost to reach the top of the floor.
Assume 0-based Indexing. You can either start from the step with index 0, or the step with index 1.

Examples:

Input: cost[] = [10, 15, 20]
Output: 15
Explanation: Cheapest option is to start at cost[1], pay that cost, and go to the top.



Input: cost[] = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest option is to start on cost[0], and only step on 1s, skipping cost[3].


Constraints:
2 ≤ cost.size() ≤ 105
0 ≤ cost[i] ≤ 999
'''

class Solution:
    def minCostClimbingStairs(self, cost):
        #Write your code here
        global dict1
        dict1=dict()
        def dp(index):
            global dict1
            if index in dict1:
                return dict1[index]
            if index==len(cost):
                return 0
            right=999
            left=dp(index+1)
            if len(cost)-index>1:
                right=dp(index+2)
            dict1[index]=cost[index]+min(left,right)
            return dict1[index]
        return min(dp(0),dp(1))