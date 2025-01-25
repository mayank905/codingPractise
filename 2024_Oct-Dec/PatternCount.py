class Solution:
    def patternCount(self, text, pattern):
        # Write your code here
        def find_all_indices(string, substring):
            indices = []
            start = 0
            while True:
                start = string.find(substring, start)
                if start == -1:
                    break
                indices.append(start)
                start += 1
            return indices
        def numSubstring(n):
            return n*(n+1)//2
        length=len(text)
        st=pattern.split('$')
        leftlength=len(st[0])
        rightlength=len(st[1])
        if leftlength:
            leftindices=find_all_indices(text,st[0])
        if rightlength:
            rightindices=find_all_indices(text,st[1])
        count=0
        if not leftlength:
            if not rightlength:
                count=numSubstring(length)
            else:
                for rightindex in rightindices:
                    count+=rightindex
        elif not rightlength:
            for leftindex in leftindices:
                diff=length-(leftindex+leftlength-1)-1
                count+=diff
        else:
            i=0
            j=0
            while i<len(leftindices) and j<len(rightindices):
                if (leftindices[i]+leftlength-1)<rightindices[j]-1:
                    count+=len(rightindices)-j
                    i+=1
                else:
                    j+=1
        return count
        
sol=Solution()
text='vdrstdkycbyeqbcad'
pattern='y$cbyeqbcad'
text='obdjwvzexcmskqekbryfnevrnwswapkytmagkopeqkxnjsyvonverlky'
pattern='ky$y'
print(sol.patternCount(text,pattern))