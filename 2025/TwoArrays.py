class Solution:
    def findMinMembers(self, a, b):
        # code here
        count=0
        length1=len(a)
        length2=len(a)
        while a and b:
            if a[length1-1]==b[length2-1]:
                a.pop()
                b.pop()
                length1-=1
                length2-=1
            else:
                count+=1
                a.pop()
                length1-=1
        return count
sol=Solution()
a=[1, 4, 2, 5, 3]
b=[4, 5, 1, 2, 3]
print(sol.findMinMembers(a,b))