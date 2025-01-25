class Solution:
    def minChar(self, s):
        # Write your code here
        revs=s[::-1]
        mix=s+'#'+revs
        totalLength=len(mix)
        lps=[0]*totalLength
        i=1
        length=0
        while i<totalLength:
            if mix[i]==mix[length]:
                length+=1
                lps[i]=length
                i+=1
            else:
                if length!=0:
                    length=lps[length-1]
                else:
                    lps[i]=0
                    i+=1
        return len(s)-lps[-1]
    


sol = Solution()
s = 'aacecaafg'
print(sol.minChar(s))

'''
class Solution:
    def minChar(self, s):
        #Write your code here
        length = len(s)
        revs = s[::-1]
        
        for i in range(length):
            if s[:length - i] == revs[i:]:
                return i
        return length - 1
'''