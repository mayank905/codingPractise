# class Solution:
#     def numWays(self, n: int, k: int, m: int) -> int:
#         #code here
#         def coinSum(s,i,j,k1):
#             if (s,i,j,k1) in dict1:
#                 return dict1[(s,i,j,k1)]
#             if k1==0:
#                 if s%m==0:
#                     return 1
#                 else:
#                     return 0
#             elif i>j and k1!=0:
#                 return 0
#             else:
#                 curVal=coins[i]
#                 dict1[(s,i,j,k1)]=(coinSum(s+curVal,i+1,j,k1-1)+coinSum(s,i+1,j,k1))
#                 return dict1[s,i,j,k1]
            
#         coins=[i for i in range(n)]
#         dict1=dict()
#         left=0
#         MOD=(10**9)+7
#         right=n-1
#         curSum=0
#         return coinSum(curSum,left,right,k)%MOD

# class Solution:
#     def numWays(self, n, k, m):
#         def coinSum(s, i, j, k1, memo):
#             if (s, i, j, k1) in memo:
#                 return memo[(s, i, j, k1)]
#             if k1 == 0:
#                 return 1 if s % m == 0 else 0
#             if i > j:
#                 return 0
#             curVal = coins[i]
#             memo[(s, i, j, k1)] = (coinSum(s + curVal, i + 1, j, k1 - 1, memo) + coinSum(s, i + 1, j, k1, memo)) % MOD
#             return memo[(s, i, j, k1)]

#         coins = list(range(n))
#         memo = {}
#         MOD = (10**9) + 7
#         return coinSum(0, 0, n - 1, k, memo)
class Solution:
    def numWays(self, n, k, m):
        MOD = 10**9 + 7
        dp = [[0] * m for _ in range(k + 1)]
        dp[0][0] = 1 

        for coin in range(n):
            value = coin
            for i in range(k, 0, -1):
                for j in range(m):
                    dp[i][(j + value) % m] = (dp[i][(j + value) % m] + dp[i - 1][j]) % MOD
        return dp[k][0]


sol=Solution()
n=5
k=3
m=3
print(sol.numWays(n,k,m))

#please optimize the above code




