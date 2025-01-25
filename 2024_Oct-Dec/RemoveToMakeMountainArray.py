from typing import List


# def traverse(array,maximum):
#     length=len(array)
#     if length==0:
#         return -1
#     temparray=list(enumerate(array))
#     sortedarray=sorted(temparray, key=lambda x: x[1])
#     count=0
#     current=sortedarray[0]
#     for i in range(1,length):
#         if current[0]>sortedarray[i][0] or current[1]>=sortedarray[i][1]:
#             count+=1
#         else:
#             if sortedarray[i][1]==maximum:
#                 count+=1
#             current=sortedarray[i]
#     return count
    


# class Solution:
#     def minimumMountainRemovals(self, nums: List[int]) -> int:
#         set1=list(set(nums))
#         set1.sort(reverse=True)
#         finalmin=float('inf')
#         delCount=0
#         for j in range(len(set1)):
#             maximum=set1[j]
#             minDelete=float('inf')
#             length=len(nums)
#             delList=[]
#             for i in range(length):
#                 if nums[i]==maximum:
#                     delList.append(i)
#                     leftarray=nums[:i]
#                     rightarray=nums[i+1:]
#                     rightarray=rightarray[::-1]
#                     leftarraylength=traverse(leftarray,maximum)
#                     rightarraylength=traverse(rightarray,maximum)
#                     if leftarraylength==-1 or rightarraylength==-1:
#                         continue
#                     minDelete=min(leftarraylength+rightarraylength,minDelete)
                    
#             finalmin=min(minDelete+delCount,finalmin)
#             curDelCount=0
#             for ele in delList:
#                 delCount+=1
#                 nums.pop(ele-curDelCount)
#                 curDelCount+=1
#         return finalmin

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)

        lis_length = [1] * N
        lds_length = [1] * N

        # Stores the length of longest increasing subsequence that ends at i.
        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis_length[i] = max(lis_length[i], lis_length[j] + 1)

        # Stores the length of longest decreasing subsequence that starts at i.
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if nums[i] > nums[j]:
                    lds_length[i] = max(lds_length[i], lds_length[j] + 1)

        min_removals = float("inf")
        for i in range(N):
            if lis_length[i] > 1 and lds_length[i] > 1:
                min_removals = min(
                    min_removals, N - lis_length[i] - lds_length[i] + 1
                )

        return min_removals
        
sol=Solution()
# nums = [2,1,3,2,3,1]
# nums=[4,3,2,1,1,2,3,1]
# nums=[1,3,1]
# nums=[1,2,3,4,4,3,2,1]
nums =[23,47,63,72,81,99,88,55,21,33,32]
result=sol.minimumMountainRemovals(nums)
print(result)