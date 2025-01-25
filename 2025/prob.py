from typing import List


class Solution:
    def isPossible(self, arr: List[int]) -> int:
        # code here
        set1=set()
        left=0
        right=len(arr)-1
        while left<right:
            if arr[left] in set1:
                return False
            if arr[right] in set1:
                return False
            prev=arr[left]
            while left<right and arr[left]==prev:
                left+=1
            set1.add(prev)
            prev=arr[right]
            while left<right and arr[right]==prev:
                right-=1
            set1.add(prev)
        return True
sol=Solution()
arr=[1,2,3,3,4,5]
# arr=[1,2,3,2,1,1]
# arr=[1,2,3,2,3,1]
print(sol.isPossible(arr))