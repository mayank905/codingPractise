'''
Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
Note: The input strings may contain leading zeros but the output string should not have any leading zeros.

Input: s1 = "1101", s2 = "111"
Output: 10100
Explanation:
 1101
+ 111
10100
Input: s1 = "00100", s2 = "010"
Output: 110
Explanation: 
  100
+  10
  110
Constraints:
1 ≤s1.size(), s2.size()≤ 106
'''
class Solution:
	def addBinary(self, s1, s2):
		# code here
		output=''
		length=max(len(s1),len(s2))
		carry=0
		for i in range(length):
			st1='0'
			if s1:
				st1=s1[-1]
				s1=s1[:-1]
			st2='0'
			if s2:
				st2=s2[-1]
				s2=s2[:-1]
			sum1=int(st1)+int(st2)+carry
			rem=sum1%2
			carry=sum1//2
			output=str(rem)+output
		if carry==1:
			output=str(1)+output
		output=output.lstrip('0')
		return output