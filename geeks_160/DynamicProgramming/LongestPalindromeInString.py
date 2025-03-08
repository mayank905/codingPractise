'''
Given a string s, your task is to find the longest palindromic substring within s.

A substring is a contiguous sequence of characters within a string, defined as s[i...j] where 0 ≤ i ≤ j < len(s).

A palindrome is a string that reads the same forward and backward. More formally, s is a palindrome if reverse(s) == s.

Note: If there are multiple palindromic substrings with the same length, return the first occurrence of the longest palindromic substring from left to right.

Examples :

Input: s = “forgeeksskeegfor” 
Output: “geeksskeeg”
Explanation: There are several possible palindromic substrings like “kssk”, “ss”, “eeksskee” etc. But the substring “geeksskeeg” is the longest among all.
Input: s = “Geeks” 
Output: “ee”
Explanation: "ee" is the longest palindromic substring of "Geeks". 
Input: s = “abc” 
Output: “a”
Explanation: "a", "b" and "c" are longest palindromic substrings of same length. So, the first occurrence is returned.
Constraints:
1 ≤ s.size() ≤ 103
s consist of only lowercase English letters.
'''
class Solution:
    def longestPalindrome(self, s):
        # code here
        length=len(s)
        dp=[[0 for _ in range(length+1)] for _ in range(length+1)]
        
        for i in range(length):
            dp[i][i]=1
        
        start,maxlength=0,1
        
        for size in range(2,length):
            for index1 in range(length-size+1):
                index2=index1+size-1
                if s[index1]==s[index2]:
                    if size==2:
                        dp[index1][index2]=1
                    else:
                        dp[index1][index2]=dp[index1+1][index2-1]
                    if dp[index1][index2] and size>maxlength:
                        start=index1
                        maxlength=size
        return s[start:start+maxlength]
sol=Solution()
s='forgeeksskeegfor'
print(sol.longestPalindrome(s))