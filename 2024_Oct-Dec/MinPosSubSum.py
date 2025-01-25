from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        minSum=float('inf')
        length=len(nums)
        left=0
        prefixsum=[]
        prevsum=0
        for num in nums:
            prevsum+=num
            prefixsum.append(prevsum)
        j=l
        while j<=r:
            i=0
            while i<=length-j:
                if i==0:
                    cursum=prefixsum[i+j-1]
                else:
                    cursum=prefixsum[i+j-1]-prefixsum[i-1]
                if cursum<=0:
                    i+=1
                    continue
                else:
                    minSum=min(minSum,cursum)
                i+=1
            j+=1
        if minSum==float('inf'):
            return -1
        else:
            return minSum
    
sol=Solution()
nums=[3, -2, 1, 4]
l=2
r=3
print(sol.minimumSumSubarray(nums,l,r))