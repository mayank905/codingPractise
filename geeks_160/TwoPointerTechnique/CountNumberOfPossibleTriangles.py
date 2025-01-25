'''
Given an integer array arr[]. Find the number of triangles that can be formed with three different array elements as lengths of three sides of the triangle. 

A triangle with three given sides is only possible if sum of any two sides is always greater than the third side.

Examples:

Input: arr[] = [4, 6, 3, 7]
Output: 3
Explanation: There are three triangles possible [3, 4, 6], [4, 6, 7] and [3, 6, 7]. Note that [3, 4, 7] is not a possible triangle.  
Input: arr[] = [10, 21, 22, 100, 101, 200, 300]
Output: 6
Explanation: There can be 6 possible triangles: [10, 21, 22], [21, 100, 101], [22, 100, 101], [10, 100, 101], [100, 101, 200] and [101, 200, 300]
Input: arr[] = [1, 2, 3]
Output: 0
Explanation: No triangles are possible.
Constraints:
3 <= arr.size() <= 103
1 <= arr[i] <= 105


'''
class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        def triangles(low,target):
            high=len(arr)-1
            while low<=high:
                mid=(low+high)//2
                if arr[mid]>=target:
                    high=mid-1
                else:
                    low=mid+1
            return low
        arr.sort()
        count=0
        for i in range(len(arr)-2):
            for j in range(i+1,len(arr)-1):
                sum1=arr[i]+arr[j]
                count+=triangles(j+1,sum1)-(j+1)
        return count


sol=Solution()
arr=[4, 6, 3, 7]
arr=[10, 21, 22, 100, 101, 200, 300]
arr=[1, 2, 3]
print(sol.countTriangles(arr))