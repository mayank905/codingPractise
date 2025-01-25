'''
Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.

Examples:

Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.
Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.
Constraints:
1 <= arr.size() <= 106
0 <= arr[i] <= 2
'''

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        zero=0
        ones=0
        for i in range(len(arr)):
            if arr[i]==0:
                arr[zero]=0
                zero+=1
            elif arr[i]==1:
                ones+=1

        j=zero
        k=1
        while j<len(arr):
            if k<=ones:
                arr[j]=1
                k+=1
            else:
                arr[j]=2
            j+=1