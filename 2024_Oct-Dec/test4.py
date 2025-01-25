class Solution:
    def findSmallest(self, s : str, k : int) -> str:
        # code here
        left=0
        right=len(s)-1
        nstring=[ord('a')]*(right+1)
        while k>0 and left<right:
            if s[left]==s[right]:
                nstring[left]=ord(s[left])-ord('a')
                nstring[right]=nstring[left]
                left+=1
                right-=1
            else:
                a=ord(s[left])-ord('a')
                b=ord(s[right])-ord('a')
                diff=abs(a-b)
                min_diff = min(diff, 26 - diff)
                a=min(a,b)
                if k>=min_diff:
                    k-=min_diff
                    nstring[left]=a
                    nstring[right]=a
                    left+=1
                    right-=1
                else:
                    return ""
                
        left=0
        right=len(s)-1
        while k>0:
            min1=min(nstring[left],26-nstring[left])
            k=k-min(k,2*min1)
            nstring[left]=chr(nstring[left]-min1+ord('a'))
            nstring[right]=nstring[left]
            left+=1
            right-=1
        for i in range(len(s)):
            if isinstance(nstring[i],int):
                nstring[i]=chr(nstring[i]+ord('a'))
        return "".join(nstring)
sol=Solution()
s='abcd'
k=2
print(sol.findSmallest(s,k))