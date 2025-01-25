'''
Given an array arr[] of non-negative integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.

Examples:

Input: arr[] = [2, 6, 1, 9, 4, 5, 3]
Output: 6
Explanation: The consecutive numbers here are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest consecutive subsquence.
Input: arr[] = [1, 9, 3, 10, 4, 20, 2]
Output: 4
Explanation: 1, 2, 3, 4 is the longest consecutive subsequence.
Input: arr[] = [15, 13, 12, 14, 11, 10, 9]
Output: 7
Explanation: The longest consecutive subsequence is 9, 10, 11, 12, 13, 14, 15, which has a length of 7.
Constraints:
1 <= arr.size() <= 105
0 <= arr[i] <= 105
'''
from collections import Counter
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        set1=set()
        max1=0
        count=Counter(arr)
        for num in arr:
            if num in set1:
                continue
            else:
                set1.add(num)
                curmax=1
                temp=num+1
                while count[temp]:
                    set1.add(temp)
                    curmax+=1
                    temp+=1
                temp=num-1
                while count[temp]:
                    set1.add(temp)
                    curmax+=1
                    temp-=1
            max1=max(max1,curmax)
        
        return max1