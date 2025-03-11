'''
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count=0
        set1=set()
        dict1=dict()
        i=0
        j=0
        while j <len(s):
            if len(set1)!=3:
                set1.add(s[j])
                dict1[s[j]]=dict1.get(s[j],0)+1
            while len(set1)==3:
                count+=len(s)-j
                dict1[s[i]]-=1
                if not dict1[s[i]]:
                    set1.remove(s[i])
                i+=1
            j+=1
        return count
    
#Better Solution 
'''
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Track last position of a, b, c
        last_pos = [-1] * 3
        total = 0

        for pos in range(len(s)):
            # Update last position of current character
            last_pos[ord(s[pos]) - ord("a")] = pos

            # Add count of valid substrings ending at current position
            # If any character is missing, min will be -1
            # Else min gives leftmost required character position
            total += 1 + min(last_pos)

        return total
'''
    
sol=Solution()
s='abcabc'
print(sol.numberOfSubstrings(s))
s="aaacb"
print(sol.numberOfSubstrings(s))
s="abc"
print(sol.numberOfSubstrings(s))