'''
Given a string s, find the length of the longest substring with all distinct characters. 

Examples:

Input: s = "geeksforgeeks"
Output: 7
Explanation: "eksforg" is the longest substring with all distinct characters.
Input: s = "aaa"
Output: 1
Explanation: "a" is the longest substring with all distinct characters.
Input: s = "abcdefabcbb"
Output: 6
Explanation: The longest substring with all distinct characters is "abcdef", which has a length of 6.
Constraints:
1<= s.size()<=3*104
All the characters are in lowercase.
'''
class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        dict1=dict()
        left=0
        maxdis=0
        for right in range(len(s)):
            if s[right] in dict1:
                left=max(left,dict1[s[right]]+1)
            dis=right-left+1
            maxdis=max(maxdis,dis)
            dict1[s[right]]=right
        return maxdis
sol=Solution()
s='fqvjgwdhmrgqkamm'
# s='geeksforgeeks'
print(sol.longestUniqueSubstr(s))