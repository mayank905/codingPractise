from collections import defaultdict
class Solution:
    def findTriplets(self, arr):
        # Your code here
        length=len(arr)
        result=[]
        dict1=defaultdict(list)
        for i in range(length):
            dict1[arr[i]].append(i)
            
        for i in range(length-2):
            for j in range(i+1,length-1):
                sum1=arr[i]+arr[j]
                for k in dict1[-sum1]:
                    if k>j:
                        result.append([i,j,k])

        return result
    
'''
Given an array arr[], find all possible indices [i, j, k] of triplets [arr[i], arr[j], arr[k]] in the array whose sum is equal to zero. Return indices of triplets in any order and all the returned triplets indices should also be internally sorted, i.e., for any triplet indices [i, j, k], the condition i < j < k should hold.

Note: Try to solve this using the O(n2) approach.
'''