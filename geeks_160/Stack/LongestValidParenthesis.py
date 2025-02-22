'''
Given a string s consisting of opening and closing parenthesis '(' and ')'. Find the length of the longest valid parenthesis substring.

A parenthesis string is valid if:

For every opening parenthesis, there is a closing parenthesis.
The closing parenthesis must be after its opening parenthesis.
Examples :

Input: s = "((()"
Output: 2
Explanation: The longest valid parenthesis substring is "()".
Input: s = ")()())"
Output: 4
Explanation: The longest valid parenthesis substring is "()()".
Input: s = "())()"
Output: 2
Explanation: The longest valid parenthesis substring is "()".
Constraints:
1 ≤ s.size() ≤ 106  
s consists of '(' and ')' only
'''

class Solution:
    def maxLength(self, s):
        # code here
        invalid=[]
        i=0
        for ch in s:
            if ch=='(':
                invalid.append((i,ch))
            else:
                if invalid and invalid[-1][1]=='(':
                    invalid.pop()
                else:
                    invalid.append((i,ch))
            i+=1
        maxdis=0
        length=len(s)
        if not invalid:
            return length
        prev=-1
        for tup in invalid:
            index=tup[0]
            dis=index-(prev+1)
            maxdis=max(maxdis,dis)
            prev=index
        maxdis=max(maxdis,length-(prev+1))
        return maxdis
sol=Solution()
s="((((()(()(())))()(()(()((()(((())()((())(())()))))(()((()(()()))((((())))))))))))())))(((()())))()))())((()())(())))((()))()(((()((()(()(())(()((((()(((()(()(()()()((((())"
print(sol.maxLength(s))