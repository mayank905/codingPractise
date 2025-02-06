'''
Given an array of integers arr[] representing non-negative integers, arrange them so that after concatenating all of them in order, it results in the largest possible number. Since the result may be very large, return it as a string.

Examples:

Input: arr[] = [3, 30, 34, 5, 9]
Output: "9534330"
Explanation: Given numbers are [3, 30, 34, 5, 9], the arrangement "9534330" gives the largest value.
Input: arr[] = [54, 546, 548, 60]
Output: "6054854654"
Explanation: Given numbers are [54, 546, 548, 60], the arrangement "6054854654" gives the largest value.
Input: arr[] = [3, 4, 6, 5, 9]
Output: "96543"
Explanation: Given numbers are [3, 4, 6, 5, 9], the arrangement "96543" gives the largest value.
Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 105
'''

from functools import cmp_to_key
class Solution:

    def findLargest(self,arr):
        # code here
        res=list(filter(lambda x:x!=0,arr))
        if res:
            res.sort(key=cmp_to_key(lambda x,y: 1 if str(x)+str(y)<str(y)+str(x) else -1))
            return ''.join(map(str,res))
        else:
            return '0'
sol=Solution()
arr = [3, 30, 34, 5, 9]
arr=[54, 542, 548, 60]
arr=[0, 0, 0, 0, 0, 0, 0, 0]
print(sol.findLargest(arr))  # Output: "9534330"