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
        set1=set()
        left=0
        length=1
        for right in range(len(s)):
            if s[right] in set1:
                length=max(length,right-left)
                while s[right] in set1:
                    set1.remove(s[left])
                    left+=1
            set1.add(s[right])
        length=max(length,right-left+1)
        return length