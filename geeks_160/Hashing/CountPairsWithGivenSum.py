'''
Given an array arr[] and an integer target. You have to find numbers of pairs in array arr[] which sums up to given target.

Examples:

Input: arr[] = [1, 5, 7, -1, 5], target = 6 
Output: 3
Explanation: Pairs with sum 6 are (1, 5), (7, -1) and (1, 5). 
Input: arr[] = [1, 1, 1, 1], target = 2 
Output: 6
Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1).
Input: arr[] = [10, 12, 10, 15, -1], target = 125
Output: 0
Constraints:
1 <= arr.size() <= 105
-104 <= arr[i] <= 104
1 <= target <= 104
'''
class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        dict1=dict()
        for i in range(len(arr)):
            if arr[i] in dict1:
                prev=dict1[arr[i]][1]+1
                dict1[arr[i]]=(i,prev)
            else:
                dict1[arr[i]]=(i,1)
        count=0
        for i in range(len(arr)):
            rem=target-arr[i]
            if rem in dict1:
                cur=dict1[rem]
                if rem==arr[i]:
                     count+=cur[1]-1
                     dict1[rem]=(cur[0],cur[1]-1)
                
                elif cur[0]>i:
                    count+=cur[1]
                    cur=dict1[arr[i]]
                    dict1[arr[i]]=(cur[0],cur[1]-1)
        return count
sol=Solution()
arr=[5, 6, 5, 7, 7, 8]
# arr=[1,5,1,5]
target=13
print(sol.countPairs(arr,target))