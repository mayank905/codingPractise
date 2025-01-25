class Solution:
    def minOps(self, a : int, b : int, c : int) -> int:
        # code here
        BPlusC=b+c
        APlusC=a+c
        APlusB=a+b
        
        # sol1=(+1)//2
        # diff=abs(BPlusC-2*a)+1
        # sol1=diff//2

        # sol2=(abs(APlusC-2*b)+1)//2
        # sol3=(abs(APlusB-2*c)+1)//2
        
        # return min(sol1,sol2,sol3)
        
        workList=[(a,BPlusC),(b,APlusC),(c,APlusB)]
        minoperation=float('inf')
        for work in workList:
            minwork=0
            if work[1]%2!=0:
                work1=(work[1]+1)//2
                work2=(work[1]-1)//2
                if (work[1]<=0 and work[0]>0) or (work[0]<=0 and work[1]>0):
                    diff1=abs(work1-work[0])
                    diff2=abs(work2-work[0])
                else:
                    diff1=abs(work1-work[0])
                    diff2=abs(work2-work[0])
                minwork=min(diff1,diff2)+1
            else:
                work1=work[1]//2
                minwork=abs(work1-work[0])
            minoperation=min(minwork,minoperation)
        return minoperation  

sl=Solution()
# inputs=[-1,-8,3] #2
inputs=[-33059,2669031,-333316]
result=sl.minOps(inputs[0],inputs[1],inputs[2])
print(result)