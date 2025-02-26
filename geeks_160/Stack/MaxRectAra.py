'''
You are given a histogram represented by an array arr, where each element of the array denotes the height of the bars in the histogram. All bars have the same width of 1 unit.

Your task is to find the largest rectangular area possible in the given histogram, where the rectangle can be formed using a number of contiguous bars.

Examples:

Input: arr[] = [60, 20, 50, 40, 10, 50, 60]
 Largest-Rectangular-Area-in-a-Histogram
Output: 100
Explanation: We get the maximum by picking bars highlighted above in green (50, and 60). The area is computed (smallest height) * (no. of the picked bars) = 50 * 2 = 100.
Input: arr[] = [3, 5, 1, 7, 5, 9]
Output: 15
Explanation:  We get the maximum by picking bars 7, 5 and 9. The area is computed (smallest height) * (no. of the picked bars) = 5 * 3 = 15.
Input: arr[] = [3]
Output: 3
Explanation: In this example the largest area would be 3 of height 3 and width 1.
Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 104
'''
# class Solution:
#     def getMaxArea(self,arr):
#         #code here
#         stack=[(0,arr[0])]
#         length=len(arr)
#         mintill=(0,347)
#         maxarea=min(arr)*length
#         for i in range(1,len(arr)):
#             index=i
#             while stack and stack[-1][1]>arr[i]:
#                 curarea=arr[i]*(i-stack[-1][0]+1)
#                 maxarea=max(maxarea,curarea)
#                 index-=1
#                 stack.pop()
#             if stack:
#                 curarea1=stack[-1][1]*(i-stack[-1][0]+1)
#                 curarea2=mintill[1]*(i-mintill[0]+1)
#                 maxarea=max(maxarea,curarea1,curarea2)
#                 mintill=stack[-1]
#             stack.append((index,arr[i]))
            
#         return maxarea
class Solution:
    def getMaxArea(self, arr):
        stack = []
        max_area = 0
        index = 0

        while index < len(arr):
            if not stack or arr[stack[-1]] <= arr[index]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                area = (arr[top_of_stack] *
                        ((index - stack[-1] - 1) if stack else index))
                max_area = max(max_area, area)

        while stack:
            top_of_stack = stack.pop()
            area = (arr[top_of_stack] *
                    ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)

        return max_area
sol=Solution()
arr=[60, 20, 50, 40, 10, 50, 60]
# arr=[3,5,1,7,5,9]
# arr=[3]
# arr=[347, 411, 476, 253, 314, 495, 959, 158, 541] #1771
print(sol.getMaxArea(arr))