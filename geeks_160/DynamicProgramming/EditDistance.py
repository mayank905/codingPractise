'''
Given two strings s1 and s2. Return the minimum number of operations required to convert s1 to s2.
The possible operations are permitted:

Insert a character at any position of the string.
Remove any character from the string.
Replace any character from the string with any other character.
Examples:

Input: s1 = "geek", s2 = "gesek"
Output: 1
Explanation: One operation is required, inserting 's' between two 'e' in s1.
Input: s1 = "gfg", s2 = "gfg"
Output: 0
Explanation: Both strings are same.
Input: s1 = "abcd", s2 = "bcfe"
Output: 3
Explanation: We can convert s1 into s2 by removing ‘a’, replacing ‘d’ with ‘f’ and inserting ‘e’ at the end. 
Constraints:
1 ≤ s1.length(), s2.length() ≤ 103
Both the strings are in lowercase.
'''
#Bottom-Up Approach
class Solution:
    def editDistance(self, s1, s2):
        len1 = len(s1)
        len2 = len(s2)
        
        # Create a 2D array to store the edit distances
        dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        
        # Initialize the base cases
        for i in range(len1 + 1):
            dp[i][0] = i
        for j in range(len2 + 1):
            dp[0][j] = j
        
        # Fill the dp array
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],    # Remove
                                       dp[i][j - 1],    # Insert
                                       dp[i - 1][j - 1]) # Replace
        
        return dp[len1][len2]
    
#Top-Down Approach
class Solution:
    def editDistance(self, s1, s2):
        memo = {}
        
        def dp(ind1, ind2):
            if (ind1, ind2) in memo:
                return memo[(ind1, ind2)]
            
            if ind1 == len(s1):
                return len(s2) - ind2
            if ind2 == len(s2):
                return len(s1) - ind1
            
            if s1[ind1] == s2[ind2]:
                memo[(ind1, ind2)] = dp(ind1 + 1, ind2 + 1)
            else:
                insert_op = dp(ind1, ind2 + 1)
                remove_op = dp(ind1 + 1, ind2)
                replace_op = dp(ind1 + 1, ind2 + 1)
                memo[(ind1, ind2)] = 1 + min(insert_op, remove_op, replace_op)
            
            return memo[(ind1, ind2)]
        
        return dp(0, 0)

# Example usage
sol = Solution()
s1 = "abcd"
s2 = "bcfe"
print(sol.editDistance(s1, s2))  # Output: 3

s1 = "geek"
s2 = "gesek"
print(sol.editDistance(s1, s2))  # Output: 1

s1 = "gfg"
s2 = "gfg"
print(sol.editDistance(s1, s2))  # Output: 0