'''
Given two sorted arrays a[] and b[] and an element k, the task is to find the element that would be at the kth position of the combined sorted array.

Examples :

Input: a[] = [2, 3, 6, 7, 9], b[] = [1, 4, 8, 10], k = 5
Output: 6
Explanation: The final combined sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.
Input: a[] = [100, 112, 256, 349, 770], b[] = [72, 86, 113, 119, 265, 445, 892], k = 7
Output: 256
Explanation: Combined sorted array is [72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892]. The 7th element of this array is 256.
Constraints:

1 <= a.size(), b.size() <= 106
1 <= k <= a.size() + b.size()
0 <= a[i], b[i] < 108
'''
# Simple Approach
'''class Solution:

    def kthElement(self, a, b, k):
        lengtha=len(a)
        lengthb=len(b)
        i=0
        j=0
        while k>0:
            if i<lengtha and j<lengthb:
                if a[i]<b[j]:
                    prev=a[i]
                    i+=1
                else:
                    prev=b[j]
                    j+=1
            elif i<lengtha:
                prev=a[i]
                i+=1
            else:
                prev=b[j]
                j+=1
            k-=1
        return prev
        pass'''

# Efficient Approach
# class Solution:
#     def kthElement(self, a, b, k):
#         lengtha = len(a)
#         lengthb = len(b)
#         if lengtha > lengthb:
#             return self.kthElement(b, a, k)
#         low = max(0, k - lengthb)
#         high = min(k, lengtha)
#         while low < high:
#             mid = (low + high) // 2
#             if a[mid] < b[k - mid - 1]:
#                 low = mid + 1
#             else:
#                 high = mid
#         return a[low] if low < lengtha else b[k - low - 1]

class Solution:

    def kthElement(self, a, b, k):
        lengtha=len(a)
        lengthb=len(b)
        if lengtha>lengthb:
            return self.kthElement(b, a, k)
        low=max(0,k-lengthb)
        high=min(k,lengtha)
        
        while low<=high:
            mid1=(low+high)//2
            mid2=k-mid1
            l1 = (mid1 == 0 and float('-inf') or a[mid1 - 1])
            r1 = (mid1 == lengtha and float('inf') or a[mid1])
            l2 = (mid2 == 0 and float('-inf') or b[mid2 - 1])
            r2 = (mid2 == lengthb and float('inf') or b[mid2])
            if l1<=r2 and l2<=r1:
                return max(l1,l2)
            if l1>r2:
                high=mid1-1
            else:
                low=mid1+1
        return 0
sol=Solution()
k=2
a=[5, 5, 8, 8, 8, 9, 11, 11, 11, 11, 11]
b=[4, 4, 4, 4, 6, 8, 9, 9, 9, 11, 13]
print(sol.kthElement(a,b,k))