'''
Given an array arr[] such that each element is in the range [0, 9] find the minimum possible sum of two numbers formed using the elements of the array. All digits in the given array must be used to form the two numbers. Return a string without leading zeroes.

Examples :

Input: arr[] = [6, 8, 4, 5, 2, 3]
Output: "604"
Explanation: The minimum sum is formed by numbers 358 and 246.
Input: arr[] = [5, 3, 0, 7, 4]
Output: "82"
Explanation: The minimum sum is formed by numbers 35 and 047.
Input: arr[] = [9, 4]
Output: "13"
Explanation: The minimum sum is formed by numbers 9 and 4.
Constraints:
1 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 9
'''
# import sys
# sys.set_int_max_str_digits(0)
# class Solution:
#     def minSum(self, arr):
#         # code here
#         num1=''
#         num2=''
#         arr.sort()
#         for i in range(len(arr)):
#             if i%2==0:
#                 num1+=str(arr[i])
#             else:
#                 num2+=str(arr[i])
#         if num2:
#             num2=int(num2)
#         else:
#             num2=0
#         total=int(num1)+int(num2)
#         return str(total)

from collections import deque
class Solution:
    def minSum(self, arr):
        n=len(arr)
        arr.sort(reverse=True)
        ans=deque()
        carry=0
        i=0
        while i<n and arr[i]!=0:
            val=arr[i]+carry
            if (i+1)<n:
                val+=arr[i+1]
            carry=val//10
            val=val%10
            ans.appendleft(str(val))
            i+=2
        if carry:
            ans.appendleft("1")
        return "".join(ans)
sol=Solution()
arr=[6, 8, 4, 5, 2, 3]
print(sol.minSum(arr))  # Output: 604