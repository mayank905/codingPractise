'''
Given an array arr[] of integers where each element represents a pile of bananas, and Koko has k hours to finish all the piles, find the minimum number of bananas (s) Koko must eat per hour to finish all the bananas within k hours. Each hour, Koko chooses a pile and eats s bananas from it. If the pile has fewer than s bananas, she consumes the entire pile for that hour and won't eat any other banana during that hour.

Examples:

Input: arr[] = [3, 6, 7, 11] , k = 8
Output: 4
Explanation: Koko eats at least 4 bananas per hour to finish all piles within 8 hours, as she can consume each pile in 1 + 2 + 2 + 3 = 8 hours.
Input: arr[] = [30, 11, 23, 4, 20], k = 5
Output: 30
Explanation: With 30 bananas per hour, Koko completes each pile in 1 hour, totaling 5 hours, which matches k = 5.
Input: arr[] = [5, 10, 15, 20], k = 7
Output: 10
Explanation: At 10 bananas per hour, Koko finishes in 7 hours, just within the k = 7 limit.
Constraint:
1 <= arr.size() <= 105 
1 <= arr[i] <= 104
arr.size() <= k <= 2*105
'''

class Solution:
    def kokoEat(self,arr,k):
        # Code here
        def check(num):
            count=0
            for n in arr:
                count+=n//num
                if n%num:
                    count+=1
            return count<=k
                
        left=1
        right=max(arr)
        while left<=right:
            mid=(left+right)//2
            if check(mid):
                right=mid-1
            else:
                left=mid+1
        return left
    
sol=Solution()
arr=[1,5]
k=5
print(sol.kokoEat(arr,k))