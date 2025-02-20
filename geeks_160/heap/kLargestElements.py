'''
Given an array arr[] of positive integers and an integer k, Your task is to return k largest elements in decreasing order. 

Examples:

Input: arr[] = [12, 5, 787, 1, 23], k = 2
Output: [787, 23]
Explanation: 1st largest element in the array is 787 and second largest is 23.
Input: arr[] = [1, 23, 12, 9, 30, 2, 50], k = 3 
Output: [50, 30, 23]
Explanation: Three Largest elements in the array are 50, 30 and 23.
Input: arr[] = [12, 23], k = 1
Output: [23]
Explanation: 1st Largest element in the array is 23.
Constraints:
1 ≤ k ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
'''
import heapq
class Solution:
	def kLargest(self, arr, k):
		# Your code here
		h=[]
		result=[]
		for num in arr:
			heapq.heappush(h,-num)
		while k:
			result.append(-heapq.heappop(h))
			k-=1
		return result
sol=Solution()
arr=[12, 5, 787, 1, 23]
k=2
print(sol.kLargest(arr,k))