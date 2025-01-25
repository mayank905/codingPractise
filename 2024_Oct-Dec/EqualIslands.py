from typing import List
# /////////////////////////////////////////////////copied Solution 1 ///////////////////////////////////////////////////////////////////////
class Solution:
    def isEqual(self, n : int, q : int, A : List[int], queries : List[List[int]]) -> int:
        def canSplit(target, importances):
            if target < 0 or not importances:
                return False
            if not target:
                return True
            
            return canSplit(target - importances[0], importances[1:]) or canSplit(target, importances[1:])
            
        
        attached = [[] for i in range(n)]
        counted = [False] * n
        
        for q in queries:
            attached[q[1] - 1].append(q[0] - 1)
            attached[q[0] - 1].append(q[1] - 1)
        
        importances = []
        
        for i in range(n):
            if not counted[i]:
                importance = A[i]
                counted[i] = True
                toVisit = attached[i]
                while toVisit:
                    nextIsland = toVisit.pop()
                    importance += A[nextIsland]
                    counted[nextIsland] = True
                    for j in attached[nextIsland]:
                        if not counted[j]:
                            toVisit.append(j)
                importances.append(importance)
                
        total = sum(importances)
        if total % 2:
            return 0
            
        half = total // 2
        
        if canSplit(half, importances):
            return 1
        else:
            return 0
# ////////////////////////////////////////////copied solution 2//////////////////////////////////////////////////////////////////////////////////
# class DisjointSet:
#     def __init__(self,n,A):
#         self.Parent = list(range(n+1)) 
#         self.Size = [0]+A
#         self.Rank = [0] * (n+1)
#     def findParent(self,v):
#         if self.Parent[v]!=v:
#             self.Parent[v] = self.findParent(self.Parent[v])
#         return self.Parent[v]
#     def unionBySize(self,u,v):
#         pu = self.findParent(u)
#         pv = self.findParent(v)
#         if pu!=pv:
#             su = self.Size[pu]
#             sv = self.Size[pv]
#             if su>sv:
#                 self.Parent[pv]=pu
#                 self.Size[pu]+=sv
#             else:
#                 self.Parent[pu]=pv
#                 self.Size[pv]+=su
# class Solution:
#     def isEqual(self, n : int, q : int, A : List[int], queries : List[List[int]]) -> int:
#         ds = DisjointSet(n,A)
#         for q1,q2 in queries:
#             p1=ds.findParent(q1)
#             p2=ds.findParent(q2)
#             if p1!=p2:
#                 ds.unionBySize(p1,p2)
#         for i in range(1,n+1):
#             ds.findParent(i)
#         s = set(ds.Parent)
#         sizes=[]
#         for i in s:
#             sizes.append(ds.Size[i])
#         islands=sizes[1:]
#         n = len(islands)
#         total = sum(A)
#         if total % 2 != 0:
#             return 0
#         goal = total // 2

#         achievable = {0}

#         for island in islands:
#             next_achievable = set()

#             for old in achievable:
#                 new = old + island

#                 if new == goal:
#                     return 1

#                 if new < goal:
#                     next_achievable.add(new)

#             achievable |= next_achievable
#             # dump(f"{achievable=}")

#         return 0
#         # DP array to track achievable sums
#         # dp = [False] * (goal + 1)
#         # dp[0] = True  # Base case: zero sum is always achievable

#         # for island in islands:
#         #     for i in range(goal, island - 1, -1):  # Iterate in reverse
#         #         if dp[i - island]:
#         #             dp[i] = True
#         #         if dp[goal]:  # Early exit if goal is reached
#         #             return 1

#         # return 1 if dp[goal] else 0
        


# ////////////////////////////////////my solution///////////////////////////////////////        



# class Solution:
#     def isEqual(self, n : int, q : int, A : List[int], queries : List[List[int]]) -> int:
#         # code here
#         # @cache
#         # def dp(curSum,targetSum,arr):
#         #     if targetSum!=0 and len(arr)==0:
#         #         return [0,0]
#         #     if targetSum==0:
#         #         return [1,1]
#         #     currentVal=int(arr[0])
#         #     if targetSum>=currentVal:
#         #         s1=dp(curSum+currentVal,targetSum-currentVal,arr[1:])
#         #         s2=dp(curSum,targetSum,arr[1:])
#         #         if s1[0] or s2[0]:
#         #             count=min(s1[1],s2[1])
#         #             return [1,count+1]
#         #     return [0,0]

#         #   without using cache
#         def dp1(index,targetSum):
#             # global dict1
#             # global finalValues
#             # global finalLength
#             st=str(index)+str(targetSum)
#             if st in dict1:
#                 return dict1[st]
#             if targetSum!=0 and index==finalLength:
#                 dict1[st]=[0,0]
#                 return [0,0]
#             if targetSum==0:
#                 dict1[st]=[1,1]
#                 return [1,1]
#             currentVal=finalValues[index]
#             if targetSum>=currentVal:
#                 s1=dp1(index+1,targetSum-currentVal)
#                 s2=dp1(index+1,targetSum)
#                 if s1[0] or s2[0]:
#                     count=min(s1[1],s2[1])
#                     dict1[st]=[1,count+1]
#                     return [1,count+1]
#             # dict1[st]=[0,0]
#             # return [0,0]
#                 else:
#                     dict1[st]=[0,0]
#                     return [0,0]
#             else:
#                 s2=dp1(index+1,targetSum)
#                 if s2[0]:
#                     dict1[st]=[1,s2[1]+1]
#                     return [1,s2[1]+1]
#                 else:
#                     dict1[st]=[0,0]
#                     return [0,0]
        
#         totalSum=sum(A)
#         if totalSum & 1:
#             return 0
#         source=dict()
#         value=dict()
#         for j in range(n):
#             source[j]=j
#             value[j]=A[j]

#         for i in range(q):
#             left=queries[i][0]-1
#             right=queries[i][1]-1
#             curSource=source[left]
#             tempVal=value[curSource]+value[right]
#             value[curSource]=tempVal
#             value[right]=tempVal
#             source[right]=curSource
#         finalIslands=set(source.values())
#         global finalValues
#         global finalLength
#         finalValues=[]
#         # finalIslands=set([s for s in source.values()])
#         for island in finalIslands:
#             finalValues.append(value[island])
#         finalLength=len(finalValues)
#         targetSum=totalSum//2
#         # finalValues.sort(reverse=True)
#         # result=dp(0,targetSum,finalValuesString)
#         global dict1
#         dict1=dict()
#         result=dp1(0,targetSum)
#         if result[0]==1 and result[1]<n:
#             return 1
#         else:
#             return 0

sol=Solution()
# n, q, arr, queries=6, 3, [1,2,3,4,5,6], [[1,2],[2,3],[4,5]]  #0
# n, q, arr, queries=3 , 1, [2,1,3], [[1,2]]  #1
# n, q, arr, queries=3 , 1, [2,1,5], [[1,2]]  #0
n, q, arr, queries=20, 10, [2, 12, 19, 7, 6, 19, 8, 10, 12, 19, 7, 13, 16, 9, 5, 5, 19, 18, 2, 10],[[10, 14],[2, 9],[14, 11],[15, 18],[10, 8],[17, 16],[4, 12],[10, 19],[2, 20],[7, 3]] #1
print(sol.isEqual(n,q,arr,queries))



'''
Here's the extracted text from the given HTML element:

You are given n islands, each with an importance value represented by an array arr of size n (1-based indexing). The importance value of island i is given by arr[i], where arr represents the importance value of island 1, arr represents the importance value of island 2, and so on up to island n. Initially, these islands are all separate.

You are also given q queries, where each query merges two distinct islands into a single larger island. The importance value of the newly formed island after a merge will be the sum of the importance values of the two merged islands. After performing all q queries, it is guaranteed that the total number of remaining distinct islands will be less than or equal to 150.

Your task is to determine whether it is possible to split these remaining distinct islands into two non-empty groups such that the total importance value of one group is equal to the total importance value of the other group.

Example 1:

Input: n=6, q=3, arr[]=[1,2,3,4,5,6] queries[]=[[1,2],[2,3],[4,5]] 
Output: 0
Explanation: There will be three islands remaining after performing all 3 queries which are [1,2,3] with the importance value 6(1+2+3), [4,5]  with the importance value 9(4+5), and [6] with the importance value 6(6). Therefore it is impossible to merge the islands in two non-empty groups, the total importance value of one group is equal to the total importance value of the other group.

Example 2:

Input: n=3 , q=1, arr[]=[2,1,3] queries[]=[[1,2]]
Output: 1
Explanation: After performing the query of merging islands 1 and 2, will be left with two islands [1,2] with importance value 3(2+1) and [3] with importance value 3(3). Therefore there exists two non-empty groups such that the total importance value of one group is equal to the total importance value of the other group.

Your Task:
You don't have to read input or print anything. Complete the function isEqual() which takes n, q, arr and queries and returns 1 if it is possible to split the remaining islands into two non-empty groups such that the total importance value of one group is equal to the total importance value of the other group, and returns 0 otherwise

Constraints:
2<=n<=10^5
1<=q<=10^5
1<=queries[i],queries[i]<=n
1<=sum(arr)<=10^5
'''