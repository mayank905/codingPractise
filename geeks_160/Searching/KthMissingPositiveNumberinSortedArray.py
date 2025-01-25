'''
Given a sorted array of distinct positive integers arr[], we need to find the kth positive number that is missing from arr[].  

Examples :

Input: arr[] = [2, 3, 4, 7, 11], k = 5
Output: 9
Explanation: Missing are 1, 5, 6, 8, 9, 10… and 5th missing number is 9.
Input: arr[] = [1, 2, 3], k = 2
Output: 5
Explanation: Missing are 4, 5, 6… and 2nd missing number is 5.
Input: arr[] = [3, 5, 9, 10, 11, 12], k = 2
Output: 2
Explanation: Missing are 1, 2, 4, 6… and 2nd missing number is 2.
Constraints:
1 <= arr.size() <= 105
1 <= k <= 105
1 <= arr[i]<= 106
'''
class Solution:
    def kthMissing(self, arr, k):
        # code here
        length=len(arr)
        left=0
        right=length-1
        while left<=right:
            mid=(left+right)//2
            if arr[mid]-(mid+1)>=k:
                right=mid-1
            else:
                left=mid+1
        return left+k
sol=Solution()
print(sol.kthMissing([2, 3, 4, 7, 11],5))#9
print(sol.kthMissing([1, 2, 3],2))#5
print(sol.kthMissing([2,3,5,6],2))#4
print(sol.kthMissing([3, 5, 9, 10, 11, 12],2))#2
print(sol.kthMissing([1, 2, 4, 5, 7, 8],5))#11