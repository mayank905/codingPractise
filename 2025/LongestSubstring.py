class Solution:
    def findSubstring(self, s: str) -> str:
        # Code here
        from collections import Counter
        myCtr=Counter(s)
        sorted_keys=sorted(myCtr.keys())
        odd=False
        left=''
        right=''
        pending=''
        for key in sorted_keys:
            half=myCtr[key]//2
            if myCtr[key]%2==0:
                left+=key*half
                right=(key*half)+right
            else:
                if not odd:
                    left+=key*half
                    right=(key*half)+right
                    pending=key
                    odd=True
                else:
                    left+=key*half
                    right=(key*half)+right
        if odd:
            left+=pending
        return left+right
sol=Solution()
s="gmligkdlkl"
print(sol.findSubstring(s))