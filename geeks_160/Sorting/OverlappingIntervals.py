'''
Given an array of Intervals arr[][], where arr[i] = [starti, endi]. The task is to merge all of the overlapping Intervals.

Examples:

Input: arr[][] = [[1,3],[2,4],[6,8],[9,10]]
Output: [[1,4], [6,8], [9,10]]
Explanation: In the given intervals we have only two overlapping intervals here, [1,3] and [2,4] which on merging will become [1,4]. Therefore we will return [[1,4], [6,8], [9,10]].
Input: arr[][] = [[6,8],[1,9],[2,4],[4,7]]
Output: [[1,9]]
Explanation: In the given intervals all the intervals overlap with the interval [1,9]. Therefore we will return [1,9].
Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ starti ≤ endi ≤ 105
'''
class Solution:
	def mergeOverlap(self, arr):
		#Code here
		arr.sort(key=lambda x:x[0])
		prev=arr[0]
		result=[]
		for i in range(1,len(arr)):
			if arr[i][0]<=prev[1]:
				prev[1]=max(arr[i][1],prev[1])
			else:
				result.append(prev)
				prev=arr[i]
		result.append(prev)
		return result