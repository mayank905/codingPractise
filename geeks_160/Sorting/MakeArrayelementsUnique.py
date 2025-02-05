'''
Given an integer array arr[ ], your task is to find the minimum number of increment operations required to make all the array elements unique. i.e. no value in the array should occur more than once. In one operation, a value can be incremented by 1 only.

Note: The answer will always fit into a 32-bit integer.

Examples :

Input: arr[] = [3, 2, 1, 2, 1, 7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7]. It can be shown that it is impossible for the array to have all unique values with 5 or less operations.
Input: arr[] = [1, 2, 2]
Output: 1
Explanation: After one operation [2 -> 3], the array could be [1, 2, 3].
Input: arr[] = [5, 4, 3, 2, 1]
Output: 0
Explanation: All elements are unique.
Constraints:
1 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 106
'''
# from collections import Counter
# class Solution:
#     def minIncrements(self, arr): 
#         # Code here
#         count=Counter(arr)
#         arr=list(set(arr))
#         arr.sort()
#         processed=set()
#         operation=0
#         for num in arr:
#             if num in processed:
#                 continue
#             while count[num]>1:
#                 operation+=count[num]-1
#                 count[num+1]+=count[num]-1
#                 processed.add(num)
#                 if count[num+1]>0:
#                     num=num+1
#         return operation

#User function Template for python3

class Solution:
    def minIncrements(self, arr): 
        # Code here
        arr.sort()
        dict1=dict()
        count=0
        max1=0
        for num in arr:
            max1=max(max1,num)
            if num in dict1:
                max1=max1+1
                count+=max1-num
                dict1[max1]=1
            else:
                dict1[num]=1
        return count

sol=Solution()
arr=[3, 2, 1, 2, 1, 7, 500, 500, 500, 502]
print(sol.minIncrements(arr))  # Output: 6