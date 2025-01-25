class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here
        lengtha=len(a)
        lengthb=len(b)
        i,j=0,0
        result=[]
        while i<lengtha and j<lengthb:
            if a[i]<b[j]:
                result.append(a[i])
                i+=1
            elif a[i]==b[j]:
                result.append(a[i])
                i+=1
                j+=1
            else:
                result.append(b[j])
                j+=1
        if i==lengtha:
            while j<lengthb:
                result.append(b[j])
                j+=1
        if j==lengthb:
            while i<lengtha:
                result.append(a[i])
                i+=1
        return result
sol=Solution()
a=[1, 2, 3, 4, 5]
b=[1, 2, 3]
print(sol.findUnion(a,b))
