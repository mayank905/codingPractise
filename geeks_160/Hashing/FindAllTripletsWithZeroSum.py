'''
Given an array arr[], find all possible triplets i, j, k in the arr[] whose sum of elements is equals to zero. 
Returned triplet should also be internally sorted i.e. i<j<k.

Examples:

Input: arr[] = [0, -1, 2, -3, 1]
Output: [[0, 1, 4], [2, 3, 4]]
Explanation: Triplets with sum 0 are:
arr[0] + arr[1] + arr[4] = 0 + (-1) + 1 = 0
arr[2] + arr[3] + arr[4] = 2 + (-3) + 1 = 0
Input: arr[] = [1, -2, 1, 0, 5]
Output: [[0, 1, 2]]
Explanation: Only triplet which satisfies the condition is arr[0] + arr[1] + arr[2] = 1 + (-2) + 1 = 0
Input: arr[] = [2, 3, 1, 0, 5]
Output: [[]]
Explanation: There is no triplet with sum 0.
Constraints:
3 <= arr.size() <= 103
-104 <= arr[i] <= 104
'''
from collections import defaultdict


class Solution:
    def findTriplets(self, arr):
        # Your code here
        result=[]
        dict1=defaultdict(list)
        for i in range(len(arr)):
            dict1[arr[i]].append(i)
        for i in range(len(arr)-2):
            cursum=arr[i]
            for j in range(i+1,len(arr)-1):
                totalsum=cursum+arr[j]
                if -totalsum in dict1:
                    for k in dict1[-totalsum]:
                        if k>j:
                            result.append([i,j,k])
        return result
sol=Solution()
arr=[0, -1, 2, -3, 1]
# arr=[1, -2, 1, 0, 5]
# arr=[2, 3, 1, 0, 5]
print(sol.findTriplets(arr))