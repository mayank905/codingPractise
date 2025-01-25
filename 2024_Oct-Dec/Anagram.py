from collections import Counter


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        length=len(s)
        chunksize=length//k
        templist=[ s[i:i+chunksize] for i in range(0, length, chunksize) ]
        tempcounter=Counter(templist)
        targetlist=[ t[i:i+chunksize] for i in range(0, length, chunksize) ]
        targetCounter=Counter(targetlist)
        #compare the two counters
        if tempcounter==targetCounter:
            return True
        return False

sol=Solution()
s="dawdawwadwad"
t="waddawdawdaw"
k=4
print(sol.isPossibleToRearrange(s,t,k))