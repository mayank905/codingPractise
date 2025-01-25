from itertools import pairwise
from typing import List


class Solution:    
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        ans, cnt = [], 1
        print(list(enumerate(pairwise(nums), 2)))
        for i, (x, y) in enumerate(pairwise(nums), 2):
            if x + 1 == y: 
                cnt += 1
            else:
                cnt = 1        
            if i >= k:
                ans.append(y if cnt >= k else -1)
        return ans
    
sol=Solution()
nums = [1,2,3,4,3,2,5]
k = 3
print(sol.resultsArray(nums,k))