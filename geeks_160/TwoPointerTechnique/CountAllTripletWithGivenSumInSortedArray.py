'''
Given a sorted array arr[] and a target value, the task is to count triplets (i, j, k) of valid indices, such that arr[i] + arr[j] + arr[k] = target and i < j < k.

Examples:

Input: arr[] = [-3, -1, -1, 0, 1, 2], target = -2
Output: 4
Explanation: Two triplets that add up to -2 are:
arr[0] + arr[3] + arr[4] = (-3) + 0 + (1) = -2
arr[0] + arr[1] + arr[5] = (-3) + (-1) + (2) = -2
arr[0] + arr[2] + arr[5] = (-3) + (-1) + (2) = -2
arr[1] + arr[2] + arr[3] = (-1) + (-1) + (0) = -2
Input: arr[] = [-2, 0, 1, 1, 5], target = 1
Output: 0
Explanation: There is no triplet whose sum is equal to 1. 
Constraints:
3 ≤ arr.size() ≤ 103
-105 ≤ arr[i], target ≤ 105
'''
from collections import defaultdict

class Solution:
    def countTriplets(self, arr, target):
        # code here
        count=0
        length=len(arr)
        for i in range(length-2):
            j=i+1
            k=length-1
            while j<k:
                sum1=arr[i]+arr[j]+arr[k]
                if sum1==target:
                    count+=1
                    temp=j+1
                    while temp<k and arr[j]==arr[temp]:
                        count+=1
                        temp+=1
                    k-=1
                elif sum1<target:
                    j+=1
                else:
                    k-=1
        return count

# class Solution:
#     def countTriplets(self, arr, target):
#         # code here
#         dict1=defaultdict()
#         count=0
#         for i in range(len(arr)):
#             if arr[i] not in dict1:
#                 dict1[arr[i]]=[i]
#             else:
#                 dict1[arr[i]].append(i)
#         for i in range(len(arr)-2):
#             for j in range(i+1,len(arr)-1):
#                 rem=target-arr[i]-arr[j]
#                 if rem in dict1:
#                     index=self.binary_search(dict1[rem], j)
#                     count+=len(dict1[rem])-index
#         return count
#     def binary_search(self, arr, x):
#         l, r = 0, len(arr) - 1
#         while l <= r:
#             mid = l + (r - l) // 2
#             if arr[mid] <= x:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return l

sol = Solution()
arr=[-3, -1, -1, 0, 1, 2]
target=-2
# arr=[-15, -7, -5, -4, 0, 1, 5, 7, 8, 20, 20 ]
# target=1
# arr=[1, 1, 1, 1, 1, 1]
# target=3
print(sol.countTriplets(arr,target))#4