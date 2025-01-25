from collections import Counter
class Solution:
    def getOperations(self, s : str) -> int:
        chdict=Counter(s)
        operations=0
        for key in chdict.keys():
            operations+=chdict[key]//3
        return operations



sol=Solution()
# st='abdbbeghege'
st='abdbghege'
result=sol.getOperations(st)
print(result)