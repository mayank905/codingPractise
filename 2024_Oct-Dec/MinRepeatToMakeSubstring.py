# class Solution:
#     def minRepeats(self, A, B):
#         # code here 
#         lengthM=len(B)
#         length=len(A)
#         index=0
#         match=False
#         for i in range(length):
#             if A[i:]==B[:length-i]:
#                 index=i
#                 match=True
#                 break
#         if not match:
#             return -1
#         cur=index
#         prevIndex=index
#         if index==0:
#             count=0
#         else:
#             count=1
#         for j in range(lengthM):
            
#             if B[j]==A[cur]:
#                 index+=1
#                 cur=index%length
#                 if cur==0:
#                     count+=1
#                 continue
#             else:
#                 return -1
#         if cur>0 and prevIndex==0:
#             count+=1
#         return count
class Solution:
    def minRepeats(self, s1, s2):
        # code here 
        origlengths1=len(s1)
        lengths2=len(s2)
        lengths1=origlengths1
        if lengths2>lengths1:
            count=lengths2//lengths1+((lengths2%lengths1)!=0)
            s1*=count
            lengths1*=count
        if lengths1==lengths2:
            if s1==s2:
                return lengths1//origlengths1
            else:
                s1+=s1[:origlengths1]
                lengths1+=origlengths1
        if lengths1>lengths2:
            diff=lengths1-lengths2
            if diff>=origlengths1:
                for i in range(diff+1):
                    if s1[i:i+lengths2]==s2:
                        return lengths1//origlengths1
                return -1
            for i in range(lengths1):
                if s1[:lengths2]==s2:
                    if i!=0:
                        s1+=s1[:origlengths1]
                        lengths1+=origlengths1
                    return lengths1//origlengths1
                s1=s1[-1]+s1[:lengths1-1]
            return -1

sol=Solution()
s1="aabaa"
s2="aaab"
# s1="abcd"
# s2="cdabcdab"
s1="abcde"
s2="cdea"
print(sol.minRepeats(s1,s2))