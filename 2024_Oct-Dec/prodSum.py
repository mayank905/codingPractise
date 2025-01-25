class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while n<=100:
            prod=1
            temp=n
            while temp:
                prod*=temp%10
                temp=temp//10
            if prod%t==0:
                return n
            n+=1
sol=Solution()
print(sol.smallestNumber(19,7))