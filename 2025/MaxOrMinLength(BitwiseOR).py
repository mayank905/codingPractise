'''
class Solution:
    def minLength(self, arr):
        # code here
        bits=[0]*11
        newarr=[]
        arr=list(set(arr))
        for num in arr:
            temp=[]
            i=0
            while num:
                if num & 1:
                    temp.append(i)
                    bits[i]+=1
                i+=1
                num>>=1
            newarr.append(temp)
        count=0
        set1=set()
        for i in range(len(arr)):
            cur=newarr[i]
            for index in cur:
                if index in set1:
                    continue
                if bits[index]-1==0:
                    bits[index]-=1
                    count+=1
                    set1.update(cur)
                    break
                else:
                    bits[index]-=1
        return count
    '''
#Solution2
# class Solution:
#     def minLength(self, arr):
#         # code here
#         bits=[0]*11
#         arr=list(set(arr))
#         arr.sort(reverse=True)
#         count=0
#         for num in arr:
#             i=0
#             cur=False
#             while num:
#                 if num & 1:
#                     if bits[i]==0:
#                         bits[i]=1
#                         cur=True
#                 i+=1
#                 num>>=1
#             if cur:
#                 count+=1
        
class Solution:
    def minLength(self, arr):
        # code here
        bits = [0] * 32  # Adjusted to handle larger numbers
        arr = list(set(arr))
        arr.sort(reverse=True)
        count = 0
        for num in arr:
            i = 0
            cur = False
            while num:
                if num & 1:
                    if bits[i] == 0:
                        bits[i] = 1
                        cur = True
                i += 1
                num >>= 1
            if cur:
                count += 1

        return count

sol = Solution()
arr = [43, 1, 37, 12, 12, 3, 35, 10, 15, 45, 36, 33, 41, 22, 5, 22, 48, 39, 25, 28, 12, 7, 22]
print(sol.minLength(arr))  # Expected output: 2
sol=Solution()
arr=[43, 1, 37, 12, 12, 3, 35, 10, 15, 45, 36, 33, 41, 22, 5, 22, 48, 39, 25, 28, 12, 7, 22]
print(sol.minLength(arr))