class Solution:
    def takeCharacters(self, text: str, req: int) -> int:
        freq = [0] * 3
        size = len(text)
        
        for char in text:
            freq[ord(char) - ord('a')] += 1
        
        left = 0
        right = 0
        
        if freq[0] < req or freq[1] < req or freq[2] < req:
            return -1
        
        for right in range(size):
            freq[ord(text[right]) - ord('a')] -= 1
            
            if freq[0] < req or freq[1] < req or freq[2] < req:
                freq[ord(text[left]) - ord('a')] += 1
                left += 1
        
        return size - (right - left + 1)

if __name__ == '__main__':
    sol=Solution()
    # s,k="aabaaaacaabc",2
    # s,k="a",1
    # s,k="abc",1
    # s,k="aabaaaacaabc",0
    # s,k="acba",1
    s,k ="bcca",1
    print(sol.takeCharacters(s,k))

'''
You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

 

Example 1:

Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.
Example 2:

Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.
 

Constraints:

1 <= s.length <= 105
s consists of only the letters 'a', 'b', and 'c'.
0 <= k <= s.length
'''