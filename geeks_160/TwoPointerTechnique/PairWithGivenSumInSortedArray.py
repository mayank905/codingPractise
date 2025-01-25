'''
You are given an integer target and an array arr[]. You have to find number of pairs in arr[] which sums up to target. It is given that the elements of the arr[] are in sorted order.
Note: pairs should have elements of distinct indexes. 

Examples :

Input: arr[] = [-1, 1, 5, 5, 7], target = 6
Output: 3
Explanation: There are 3 pairs which sum up to 6 : {1, 5}, {1, 5} and {-1, 7}.
Input: arr[] = [1, 1, 1, 1], target = 2
Output: 6
Explanation: There are 6 pairs which sum up to 2 : {1, 1}, {1, 1}, {1, 1}, {1, 1}, {1, 1} and {1, 1}.
Input: arr[] = [-1, 10, 10, 12, 15], target = 125
Output: 0
Explanation: There is no such pair which sums up to 4.
Constraints:
-105 <= target <=105
 2 <= arr.size() <= 105
-105 <= arr[i] <= 105
'''
class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        left=0
        right=len(arr)-1
        count=0
        while left<right:
            sum1=arr[left]+arr[right]
            if sum1<target:
                left+=1
            elif sum1>target:
                right-=1
            else:
                count+=1
                temp=right-1
                while left<temp and arr[temp]==arr[right]:
                    count+=1
                    temp-=1
                left+=1
        return count