'''
Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']', verify the validity of the arrangement.
An input string is valid if:

         1. Open brackets must be closed by the same type of brackets.
         2. Open brackets must be closed in the correct order.

Examples :

Input: s = "[{()}]"
Output: true
Explanation: All the brackets are well-formed.
Input: s = "[()()]{}"
Output: true
Explanation: All the brackets are well-formed.
Input: s = "([]"
Output: False
Explanation: The expression is not balanced as there is a missing ')' at the end.
Input: s = "([{]})"
Output: False
Explanation: The expression is not balanced as there is a closing ']' before the closing '}'.
Constraints:
1 ≤ s.size() ≤ 106
s[i] ∈ {'{', '}', '(', ')', '[', ']'}
'''
class Solution:
    def isBalanced(self, s):
        # code here
        stack=[]
        openbracket={'{','[','('}
        opposite={'}':'{',']':'[',')':'('}
        for ch in s:
            if ch in openbracket:
                stack.append(ch)
            else:
                if stack and stack[-1]==opposite[ch]:
                    stack.pop()
                else:
                    return False
        return not stack
