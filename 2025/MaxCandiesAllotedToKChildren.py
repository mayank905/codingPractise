'''
You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.

You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies. Each child can be allocated candies from only one pile of candies and some piles of candies may go unused.

Return the maximum number of candies each child can get.

 

Example 1:

Input: candies = [5,8,6], k = 3
Output: 5
Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.
Example 2:

Input: candies = [2,5], k = 11
Output: 0
Explanation: There are 11 children but only 7 candies in total, so it is impossible to ensure each child receives at least one candy. Thus, each child gets no candy and the answer is 0.
 

Constraints:

1 <= candies.length <= 105
1 <= candies[i] <= 107
1 <= k <= 1012
'''
from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        candies.sort()
        sum1=sum(candies)
        max1=sum1//k
        if max1==0 or max1==1:
            return max1
        min1=0
        def func(target):
            i=0
            count=k
            for candy in candies:
                i+=candy//target
            return i>=k
        while min1<=max1:
            mid=(min1+max1)//2
            if func(mid):
                min1=mid+1
            else:
                max1=mid-1
        return max1

sol=Solution()
# candies = [5,8,6]
# k=3
# print(sol.maximumCandies(candies, k))  # Output: 5
# candies = [2,5]
# k=11
# print(sol.maximumCandies(candies, k))  # Output: 0
# candies=[4,7,5]
# k=16
# print(sol.maximumCandies(candies, k))  # Output: 4
candies=[8249021,995692,3769504,2664179,4805275,9318902,9892266,4395580,2629315]
k=45067556
print(sol.maximumCandies(candies, k))  # Output: 9892266