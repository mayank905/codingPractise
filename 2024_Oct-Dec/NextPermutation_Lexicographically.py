'''
Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.

Examples:

Input: arr = [2, 4, 1, 7, 5, 0]
Output: [2, 4, 5, 0, 1, 7]
Explanation: The next permutation of the given array is {2, 4, 5, 0, 1, 7}.
Input: arr = [3, 2, 1]
Output: [1, 2, 3]
Explanation: As arr[] is the last permutation, the next permutation is the lowest one.
Input: arr = [3, 4, 2, 5, 1]
Output: [3, 4, 5, 1, 2]
Explanation: The next permutation of the given array is {3, 4, 5, 1, 2}.
Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 10
'''
# My Failed Solution

# class Solution:
#     def nextPermutation(self, arr):
#         def maxandNextmax(arr):
#             cmax=arr[0]
#             nextMax=10**5
#             max2=0
#             for num in arr:
#                 max2=max(max2,num)
#                 if num>cmax and num<nextMax:
#                     nextMax=num
#             if max2==cmax:
#                 nextMax=-1
#             return nextMax
            
            
#         # code here
#         length=len(arr)
#         max1=max(arr)
#         nextarr=[]
#         temp=[]
#         for i in range(length-1):
#             if arr[i]<arr[i+1]:
#                 continue
#             else:
#                 temp=arr[:i].copy()
#                 nextarr=arr[i:].copy()
#                 break
#         if nextarr:
#             nextmax=maxandNextmax(nextarr)
#             if nextmax==-1:
#                 nextarr.sort()
#                 if temp:
#                     temp1=nextarr[0]
#                     nextarr[0]=temp[-1]
#                     temp[-1]=temp1
                
#                 temp.extend(nextarr)
#             else:
#                 temp.append(nextarr[0])
#                 temp.append(nextmax)
#                 nextarr=nextarr[1:]
#                 index=nextarr.index(nextmax)
#                 del nextarr[index]
#                 nextarr.sort()
#                 temp.extend(nextarr)
#             return temp
#         else:
#             return arr

#Claud LLm solution
class Solution:
   def nextPermutation(self,arr):
        """
        Rearranges numbers into the lexicographically next greater permutation.
        If no such arrangement is possible, it must rearrange it to the lowest possible order.
        Args:
            arr: List of integers
        Returns:
            None (modifies arr in-place)
        """
        n = len(arr)
        if n <= 1:
            return
        
        # Step 1: Find the first pair from right where arr[i] < arr[i+1]
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
            
        if i >= 0:
            # Step 2: Find the smallest element in right half that's greater than arr[i]
            j = n - 1
            while j >= 0 and arr[j] <= arr[i]:
                j -= 1
                
            # Step 3: Swap the elements
            arr[i], arr[j] = arr[j], arr[i]
        
        # Step 4: Reverse the right half
        left = i + 1
        right = n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr
sol=Solution()
arr=[
    [1,2,3,6,5,4], #124356
    [2,4,1,7,5,0], #245017
    [3,2,1], #123
    [3,4,2,5,1], #34512
    [1, 2, 5, 3, 4]] #12543
for ar in arr:
    print(sol.nextPermutation(ar))