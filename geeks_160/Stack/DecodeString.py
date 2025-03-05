'''
Given an encoded string s, the task is to decode it. The encoding rule is :

k[encodedString], where the encodedString inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer, and encodedString contains only lowercase english alphabets.
Note: The test cases are generated so that the length of the output string will never exceed 105 .

Examples:

Input: s = "1[b]"
Output: "b"
Explanation: "b" is present only one time.
Input: s = "3[b2[ca]]"
Output: "bcacabcacabcaca"
Explanation:
1. Inner substring “2[ca]” breakdown into “caca”.
2. Now, new string becomes “3[bcaca]”
3. Similarly “3[bcaca]” becomes “bcacabcacabcaca ” which is final result.
Constraints:
1 ≤ |s| ≤ 105 
1 <= k <= 100
'''
class Solution:
    def decodedString(self, s):
        # code here
        st=[]
        num=[]
        length=len(s)
        i=0
        curstr=''
        curnum=''
        while i<length:
            if s[i].isdigit():
                curnum+=s[i]
            elif s[i]=='[':
                st.append(curstr)
                curstr=''
                num.append(curnum)
                curnum=''
            elif s[i]==']':
                tempnum=num.pop()
                curstr*=int(tempnum)
                curstr=st.pop()+curstr
            else:
                curstr+=s[i]
            i+=1
        return curstr
                