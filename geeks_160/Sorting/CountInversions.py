'''
Given an array of integers arr[]. Find the Inversion Count in the array.
Two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum. 

Examples:

Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
Input: arr[] = [2, 3, 4, 5, 6]
Output: 0
Explanation: As the sequence is already sorted so there is no inversion count.
Input: arr[] = [10, 10, 10]
Output: 0
Explanation: As all the elements of array are same, so there is no inversion count.
Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 104
'''
class Solution:
    def inversionCount(self, arr):
        temp = [0]*len(arr)
        
        def split(arr, i, j):
            inversions = 0
            if i < j:
                m = (i+j)//2
                inversions += split(arr, i, m)
                inversions += split(arr, m+1, j)
                inversions += merge(arr, i, m, j)
            return inversions
                
        def merge(arr, i, m, j):
            p1 = i
            p2 = m+1
            pt = i
            inversions = 0
            while p1 <= m and p2 <= j:
                if arr[p1] <= arr[p2]:
                    temp[pt] = arr[p1]
                    pt += 1
                    p1 += 1
                else:
                    temp[pt] = arr[p2]
                    inversions += (m - p1 + 1)
                    pt += 1
                    p2 += 1
            while p1 <= m:
                temp[pt] = arr[p1]
                p1 += 1
                pt += 1
            while p2 <= j:
                temp[pt] = arr[p2]
                p2 += 1
                pt += 1
            arr[i:j+1] = temp[i:j+1]
            return inversions
            
        return split(arr, 0, len(arr)-1)