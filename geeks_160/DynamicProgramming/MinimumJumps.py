'''
You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.

For example:

If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
If arr[i] = 0, you cannot jump forward from that position.
Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position.

Note:  Return -1 if you can't reach the end of the array.

Examples : 

Input: arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
Output: 3 
Explanation: First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last. 
Input: arr = [1, 4, 3, 2, 6, 7]
Output: 2 
Explanation: First we jump from the 1st to 2nd element and then jump to the last element.
Input: arr = [0, 10, 20]
Output: -1
Explanation: We cannot go anywhere from the 1st element.
Constraints:
2 ≤ arr.size() ≤ 104
0 ≤ arr[i] ≤ 104
'''
class Solution:
	def minJumps(self, arr):
	    # code here
		dict1 = dict()
		def dp(index):
			if index in dict1:
				return dict1[index]
			if index == len(arr) - 1:
				return 0
			if index >= len(arr):
				return float('inf')
			if arr[index] == 0:
				return float('inf')
			for i in range(1, arr[index] + 1):
				dict1[index] = min(dict1.get(index, float('inf')), 1 + dp(index + i))
			return dict1[index]
		res = dp(0)
		return res if res != float('inf') else -1
sol=Solution()
arr=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(sol.minJumps(arr)) #3
arr=[1, 4, 3, 2, 6, 7]
print(sol.minJumps(arr)) #2
arr=[0, 10, 20]
print(sol.minJumps(arr)) #-1
			