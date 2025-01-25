'''
Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 

Examples:

Input: arr[] = [3, 0, 1, 0, 4, 0 2]
Output: 10
Explanation: Total water trapped = 0 + 3 + 2 + 3 + 0 + 2 + 0 = 10 units.

Input: arr[] = [3, 0, 2, 0, 4]
Output: 7
Explanation: Total water trapped = 0 + 3 + 1 + 3 + 0 = 7 units.
Input: arr[] = [1, 2, 3, 4]
Output: 0
Explanation: We cannot trap water as there is no height bound on both sides.
Input: arr[] = [2, 1, 5, 3, 1, 0, 4]
Output: 9
Explanation: Total water trapped = 0 + 1 + 0 + 1 + 3 + 4 + 0 = 9 units.
Constraints:
1 < arr.size() < 105
0 < arr[i] < 103
'''
# Solution 1:
'''
class Solution:
    def maxWater(self, arr):
        n=len(arr)
        left = [0]*n
        right = [0]*n
        water = 0
        left[0] = arr[0]
        for i in range(1, n):
            left[i] = max(left[i-1], arr[i])
        right[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], arr[i])
        for i in range(n):
            water += min(left[i], right[i]) - arr[i]
        return water
'''
# Solution 2:
class Solution:
    def maxWater(self, arr):
        #Code here
        n=len(arr)
        stack=[]
        sum1=0
        for i in range(n):
            if not stack and i+1<=n-1:
                if arr[i]>arr[i+1]:
                    stack.append(i)
            if stack:
                if arr[i]<=arr[i-1]:
                    stack.append(i)
                else:
                    while len(stack)>=2 and arr[i]>=arr[stack[-1]]:
                        width=i-stack[-2]-1
                        low=arr[stack.pop()]
                        height=min(arr[stack[-1]],arr[i])-low
                        sum1+=width*height
                    if arr[stack[-1]]<arr[i]:
                        stack.pop()
                    stack.append(i)
        return sum1
sol=Solution()
arr=[3, 0, 1, 0, 4, 0, 2]
print(sol.maxWater(arr)) # 10