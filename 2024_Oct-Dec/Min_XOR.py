from typing import List
import functools

class Solution:
    def minXOR(self, n : int, k : int, arr : List[int]) -> int:
        max_number = max(arr)
        bits_needed = max_number.bit_length()
        xor_value = functools.reduce(lambda x, y: x ^ y, arr)
        # binary_representations = [f'{number:0{bits_needed}b}' for number in arr]
        xor_binary_representation = f'{xor_value:0{bits_needed}b}'
        length=len(xor_binary_representation)
        l=0
        while k!=0 and l!=length-1:
            if xor_binary_representation[l]=='1':
                k-=1
                xor_binary_representation=xor_binary_representation[0:l]+'0'+xor_binary_representation[l+1:]
                l+=1
            else:
                l+=1
        if k==0:
            return int(xor_binary_representation,2)
        else:
             return 0


sol=Solution()
n=6
k=2
arr=[1,2,5,7,9,6]
# arr=[1,2,3]
result=sol.minXOR(n,k,arr)
print(result)