'''
You have a row of flowers, where each flower blooms after a specific day. The array arr represents the blooming schedule: arr[i] is the day the flower at position i will bloom. To create a bouquet, you need to collect k adjacent bloomed flowers. Each flower can only be used in one bouquet.

Your goal is to find the minimum number of days required to make exactly m bouquets. If it is not possible to make m bouquets with the given arrangement, return -1.

Examples:
Input: m = 3, k = 2, arr[] = [3, 4, 2, 7, 13, 8, 5]
Output: 8
Explanation: We need 3 bouquets and each bouquet should have 2 flowers. After day 8: [x, x, x, x, _, x, x], we can make first bouquet from the first 2 flowers, second bouquet from the next 2 flowers and the third bouquet from the last 2 flowers.
Input: m = 2, k = 3, arr[] = [5, 5, 5, 5, 10, 5, 5]
Output: 10
Explanation: We need 2 bouquets and each bouquet should have 3 flowers, After day 5: [x, x, x, x, _, x, x], we can make one bouquet of the first three flowers that bloomed, but cannot make another bouquet. After day 10: [x, x, x, x, x, x, x], Now we can make two bouquets, taking 3 adjacent flowers in one bouquet.
Input: m = 3, k = 2, arr[] = [1, 10, 3, 10, 2]
Output: -1
Explanation: As 3 bouquets each having 2 flowers are needed, that means we need 6 flowers. But there are only 5 flowers so it is impossible to get the needed bouquets therefore -1 will be returned.
Constraints:
1 <= k <= arr.size() <= 105
1 <= m <= 105
1 <= arr[i] <= 109
'''
class Solution:
    def minDaysBloom(self, m, k, arr):
        # Code here
        def check(days):
            singleBatch=0
            totalBatch=0
            for num in arr:
                if num<=days:
                    singleBatch+=1
                    if singleBatch==k:
                        totalBatch+=1
                        singleBatch=0
                else:
                    singleBatch=0
            return totalBatch>=m
            
        length=len(arr)
        if m*k>length:
            return -1
        left=1
        right=max(arr)
        while left<=right:
            mid=(left+right)//2
            if check(mid):
                right=mid-1
            else:
                left=mid+1
        return left
    

'''
Solve using Dynamic Programming, Below approach not working, although above appraoch still better
'''
# from functools import cache
# class Solution:
#     def minDaysBloom(self, m, k, arr):
#         length = len(arr)
#         global min1

#         def dp(index,curmax,rem):
#             global min1
#             if index==length:
#                 if rem==0:
#                     min1=min(curmax,min1)
#                     return 
#                 else:
#                     return
#             if rem!=0 and index+k>=length:
#                 return 
#             max1=max(arr[index:index+k])
#             dp(index+1,curmax,rem)
#             curmax=max(curmax,max1)
#             dp(index+k,curmax,rem-1)
            
            
#         min1=float('inf')
#         dp(0,0, m)
#         return min1 if min1 != float('inf') else -1

# Example usage
sol = Solution()
m = 3
k = 2
arr = [3, 4, 2, 7, 13, 8, 5]
print(sol.minDaysBloom(m, k, arr))  # Output: 8

# m = 2
# k = 3
# arr = [5, 5, 5, 5, 10, 5, 5]
# print(sol.minDaysBloom(m, k, arr))  # Output: 10

# m = 3
# k = 2
# arr = [1, 10, 3, 10, 2]
# print(sol.minDaysBloom(m, k, arr))  # Output: -1
