from functools import cache
from typing import List


# class Solution:
#     def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # @cache
        # def checkPartition(index,targetSum,k):
        #     global length
        #     if k==0:
        #         return False
        #     if targetSum<0:
        #         return False
        #     if k==1:
        #         if targetSum==0:
        #             return True
        #         elif index==length:
        #             return False
        #         else:
        #             if nums[index]<=targetSum:
        #                 bol1=checkPartition(index+1,targetSum-nums[index],k)
        #                 bol2=checkPartition(index+1,targetSum,k)
        #                 if bol1 or bol2:
        #                     return True
        #                 else:
        #                     return False
        #             else:
        #                 bol2=checkPartition(index+1,targetSum,k)
        #                 return bol2
        #     else:
        #         if targetSum%k!=0:
        #             return False
        #         firstSum=targetSum//k
        #         secondSum=targetSum-firstSum
        #         bol1=checkPartition(index+1,firstSum,1)
        #         bol2=checkPartition(index+1,secondSum-nums[index],k-1)
        #         bol3=checkPartition(index+1,firstSum-nums[index],1)
        #         bol4=checkPartition(index+1,secondSum,k-1)
        #         if (bol1 and bol2) or (bol3 and bol4):
        #             return True
        #         else:
        #             return False
                

        # global length
        # Sum1=sum(nums)
        # length=len(nums)
        # if Sum1%k!=0:
        #     return False
        # firstSum=Sum1//k
        # secondSum=Sum1-firstSum
        # bol1=checkPartition(1,firstSum,1)
        # bol2=checkPartition(1,secondSum-nums[0],k-1)
        # bol3=checkPartition(1,firstSum-nums[0],1)
        # bol4=checkPartition(1,secondSum,k-1)
        
        # if (bol1 and bol2) or (bol3 and bol4):
        #     return True
        # else:
        #     return 
class Solution:        
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k:
            return False

        reqSum = total // k
        subSets = [0] * k
        nums.sort(reverse = True)

        def recurse(i):
            if i == len(nums):    
                return True

            for j in range(k):
                if subSets[j] + nums[i] <= reqSum:
                    subSets[j] += nums[i]

                    if recurse(i + 1):
                        return True

                    subSets[j] -= nums[i]

                    # Important line, otherwise function will give TLE
                    if subSets[j] == 0:
                        break

                    """
                    Explanation:
                    If subSets[j] = 0, it means this is the first time adding values to that subset.
                    If the backtrack search fails when adding the values to subSets[j] and subSets[j] remains 0, it will also fail for all subSets from subSets[j+1:].
                    Because we are simply going through the previous recursive tree again for a different j+1 position.
                    So we can effectively break from the for loop or directly return False.
                    """

            return False

        return recurse(0)
sol=Solution()
nums =[2,2,2,2,3,4,5]
k=4
print(sol.canPartitionKSubsets(nums,k))