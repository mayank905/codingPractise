'''
Given a string s, count all palindromic sub-strings present in the string. The length of the palindromic sub-string must be greater than or equal to 2. 

Examples

Input: s = "abaab"
Output: 3
Explanation: All palindromic substrings are : "aba" , "aa" , "baab".
Input: s = "aaa"
Output: 3
Explanation: All palindromic substrings are : "aa", "aa", "aaa".
Input: s = "abbaeae"
Output: 4
Explanation: All palindromic substrings are : "bb" , "abba" , "aea", "eae".
Constraints:
2 ≤ s.size() ≤ 103
string contains only lowercase english characters
'''
class Solution:

    def countPS(self, s):
        # code here
        count=0
        length=len(s)
        dp=[[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            dp[i][i]=1
        for size in range(2,length+1):
            for left in range(length-size+1):
                right=left+size-1
                if s[left]==s[right]:
                    if size==2:
                        dp[left][right]=1
                        count+=1
                    else: 
                        dp[left][right]=dp[left+1][right-1]
                        if dp[left][right]:
                            count+=1
        return count
sol=Solution()
s='iuupntdtyoslyzrvuaasghahnvuhbjtftyrijksypvebxowukzotdrlhpzkjxntjpvcvvc'
# s='yxpkecckjhvoqfflkadfozbbxdqfpxmngzzgnmxpfqdxbbzofdaklffqovhjkccekpxy'
print(sol.countPS(s))