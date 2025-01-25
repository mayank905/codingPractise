'''
Given an array arr[] and a number target, find a pair of elements (a, b) in arr[], where a<=b whose sum is closest to target.
Note: Return the pair in sorted order and if there are multiple such pairs return the pair with maximum absolute difference. If no such pair exists return an empty array.

Examples:

Input: arr[] = [10, 30, 20, 5], target = 25
Output: [5, 20]
Explanation: As 5 + 20 = 25 is closest to 25.
Input: arr[] = [5, 2, 7, 1, 4], target = 10
Output: [2, 7]
Explanation: As (4, 7) and (2, 7) both are closest to 10, but absolute difference of (2, 7) is 5 and (4, 7) is 3. Hence, [2, 7] has maximum absolute difference and closest to target. 
Input: arr[] = [10], target = 10
Output: []
Explanation: As the input array has only 1 element, return an empty array.
Constraints:
1 <= arr.size() <= 2*105
0 <= target<= 2*105
0 <= arr[i] <= 105
'''
class Solution:
    def sumClosest(self, arr, target):
        # code here
        arr.sort()
        length=len(arr)
        min1=float('inf')
        result=[]
        i=0
        j=length-1
        while i<j:
            sum1=arr[i]+arr[j]
            if sum1==target:
                return [arr[i], arr[j]]
            elif sum1<target:
                if target-sum1<min1:
                    min1=target-sum1
                    result=[arr[i], arr[j]]
                i+=1
            else:
                if sum1-target<min1:
                    min1=sum1-target
                    result=[arr[i], arr[j]]
                j-=1
        return result
sol=Solution()
arr=[10, 30, 20, 5]
target=25
arr=[5, 2, 7, 1, 4]
target=10
arr=[1,2,3,4,5]
target=10
arr=[532, 3408, 7453, 12539, 13977, 14063, 27343, 29559, 31737, 32095]
target=3
arr=[17,19]
target=9
arr=[8, 10, 13, 2, 16, 0, 4, 6]
target=14
print(sol.sumClosest(arr, target)) # [5, 20]