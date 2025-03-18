'''
Given an array of positive integers arr[] and a value sum, determine if there is a subset of arr[] with sum equal to given sum. 

Examples:

Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 9
Output: true 
Explanation: Here there exists a subset with target sum = 9, 4+3+2 = 9.
Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 30
Output: false
Explanation: There is no subset with target sum 30.
Input: arr[] = [1, 2, 3], sum = 6
Output: true
Explanation: The entire array can be taken as a subset, giving 1 + 2 + 3 = 6.
Constraints:
1 <= arr.size() <= 200
1<= arr[i] <= 200
1<= sum <= 104
'''
class Solution:
    def isSubsetSum(self, arr, target_sum):
        n = len(arr)
        
        # Create a DP table where dp[i][j] is True if a subset of the first i elements has a sum equal to j
        dp = [[False for _ in range(target_sum + 1)] for _ in range(n + 1)]
        
        # Base case: A sum of 0 can always be achieved with an empty subset
        for i in range(n + 1):
            dp[i][0] = True
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, target_sum + 1):
                if arr[i - 1] > j:  # If the current element is greater than the target sum
                    dp[i][j] = dp[i - 1][j]
                else:
                    # Include or exclude the current element
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
        
        return dp[n][target_sum]

# Example usage
sol = Solution()
arr = [3, 34, 4, 12, 5, 2]
target_sum = 9
print(sol.isSubsetSum(arr, target_sum))  # Output: True

arr = [3, 34, 4, 12, 5, 2]
target_sum = 30
print(sol.isSubsetSum(arr, target_sum))  # Output: False

arr = [1, 2, 3]
target_sum = 6
print(sol.isSubsetSum(arr, target_sum))  # Output: True