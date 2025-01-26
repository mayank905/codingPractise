'''
We have a wooden plank of the length n units. Some ants are walking on the plank, each ant moves with a speed of 1 unit per second. Some of the ants move to the left, the other move to the right.
When two ants moving in two different directions meet at some point, they change their directions and continue moving again. Assume changing directions does not take any additional time. When an ant reaches one end of the plank at a time t, it falls out of the plank immediately.

Given an integer n and two integer arrays left[] and right[], the positions of the ants moving to the left and the right, return the moment when the last ant(s) fall out of the plank.

Examples :

Input: n = 4, left[] = [2], right[] = [0, 1, 3]
Output: 4
        
Explanation: As seen in the above image, the last ant falls off the plank at t = 4.
Input:  n = 4, left[] = [], right[] = [0, 1, 2, 3, 4]
Output: 4
        
 Explanation: All ants are going to the right, the ant at index 0 needs 7 seconds to fall.
Input: n = 3, left[] = [0], right[] = [3]
Output: 0
Explanation: The ants will fall off the plank as they are already on the end of the plank.
Constraints:
1 <= n <= 105
0 <= left.length <= n + 1
0 <= left[i] <= n
0 <= right.length <= n + 1
0 <= right[i] <= n
1 <= left.length + right.length <= n + 1
All values of left and right are unique, and each value can appear only in one of the two arrays.
'''

class Solution:
    def getLastMoment(self, n, left, right):
        #code here
        dis=0
        max1=max(left)
        min1=min(right)
        if left==[]:
            dis=n-min1
            return dis
        if right==[]:
            dis=max1
            return dis
        
        if max1>(n-min1):
            dis=max1
        else:
            dis=n-min1
        return dis
    # OR
        # max1=max(left) if left else 0
        # min1=min(right) if right else 0
        # if not left:
        #     return n-min1
        # if not right:
        #     return max1
        # if max1>=(n-min1):
        #     return max1
        # else:
        #     return n-min1 
sol=Solution()
n = 8
left = [0,8,7]
right = [3,1,2]
print(sol.getLastMoment(n,left,right))