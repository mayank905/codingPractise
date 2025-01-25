'''
Given an array of integers arr[] in a circular fashion. Find the maximum subarray sum that we can get if we assume the array to be circular.

Examples:

Input: arr[] = [8, -8, 9, -9, 10, -11, 12]
Output: 22
Explanation: Starting from the last element of the array, i.e, 12, and moving in a circular fashion, we have max subarray as 12, 8, -8, 9, -9, 10, which gives maximum sum as 22.
Input: arr[] = [10, -3, -4, 7, 6, 5, -4, -1]
Output: 23
Explanation: Maximum sum of the circular subarray is 23. The subarray is [7, 6, 5, -4, -1, 10].
Input: arr[] = [-1, 40, -14, 7, 6, 5, -4, -1] 
Output: 52
Explanation: Circular Subarray [7, 6, 5, -4, -1, -1, 40] has the maximum sum, which is 52.
Constraints:
1 <= arr.size() <= 105
-104 <= arr[i] <= 104
'''
#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    prev=0
    maxsofar=float('-inf')
    for num in arr:
        prev+=num
        if prev<num:
            prev=num
        maxsofar=max(maxsofar,prev)
    prefixsum=[]
    maxtill=[]
    max1=float('-inf')
    prev=0      
    for num in arr:
        prev+=num
        prefixsum.append(prev)
        max1=max(max1,prev)
        maxtill.append(max1)
    initmax=max(arr)
    finalmax=max(initmax,max(prefixsum),maxsofar)
    for i in range(1,len(arr)+1):
        right=prefixsum[-1]-prefixsum[i-1]
        left=maxtill[i-1]
        finalmax=max(finalmax,left+right)
    return finalmax
        
