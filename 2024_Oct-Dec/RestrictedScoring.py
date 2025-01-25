# class Solution:
#     def getCount(self, n : int) -> int:
#         # code here
#         # mem=dict()
#         def remainCount(lastHit,remainRun):
#             # if (lastHit,remainRun) in mem:
#             #     return mem[(lastHit,remainRun)]
#             if remainRun==0:
#                 return 1
#             elif remainRun<0:
#                 return 0
#             else:
#                 one=remainCount(1,remainRun-1)
#                 two=remainCount(2,remainRun-2)
#                 four=0
#                 if lastHit!=4:
#                     four=remainCount(4,remainRun-4)
#                 six=remainCount(6,remainRun-6)
#                 # mem[(lastHit,remainRun)]=one+two+four+six
#                 return one+two+four+six
                
#         return remainCount(0,n)
class Solution:
    def getCount(self, n : int) -> int:
        MOD=(10**9)+7
        dp = dict()

        dp[(0,1)]=1
        dp[(0,2)]=1
        dp[(0,4)]=1
        dp[(0,6)]=1
        for run in range(1,n+1):
            for hit in [1,2,4,6]:
                dp[(run,hit)]=0
                if run-1>=0:
                    dp[(run,hit)]+=dp[(run-1,1)]
                if run-2>=0:
                    dp[(run,hit)]+=dp[(run-2,2)]
                if hit!=4 and run-4>=0:
                    dp[(run,hit)]+=dp[(run-4,4)]
                if run-6>=0:
                    dp[(run,hit)]+=dp[(run-6,6)]
        # print(dp[(n,1)])
        # print(dp[(n,2)])
        # print(dp[(n,4)])
        # print(dp[(n,6)])
        return (dp[(n,1)])%MOD


sol=Solution()
print(sol.getCount(12))
#597598463   n=36  34012224
#367025799   n=39