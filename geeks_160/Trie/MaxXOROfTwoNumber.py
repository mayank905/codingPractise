'''
Given an array arr[] of non-negative integers of size n. Find the maximum possible XOR between two numbers present in the array.

Examples:

Input: arr[] = [25, 10, 2, 8, 5, 3]
Output: 28
Explanation: The maximum possible XOR is 5 ^ 25 = 28.
Input: arr[] = [1, 2, 3, 4, 5, 6, 7]
Output: 7
Explanation : The maximum possible XOR is 1 ^ 6 = 7.
Constraints:
2 ≤ arr.size() ≤ 5*104
1 ≤ arr[i] ≤ 106
Expected Complexities
Time Complexity: O(n log n)
Auxiliary Space: O(n)
'''
#Approach is to use Trie data structure to store the binary representation of numbers.
# We will insert the numbers in the trie and then for each number we will find the maximum xor possible with the numbers already present in the trie.

'''class Node:
    def __init__(self):
        self.zero=None
        self.one=None
class Trie:
    def __init__(self):
        self.root=Node()
        
    def insert(self,num):
        curr=self.root
        for i in range(31,-1,-1):
            bit=(num>>i)&1
            if bit==0:
                if not curr.zero:
                    curr.zero=Node()
                curr=curr.zero
            else:
                if not curr.one:
                    curr.one=Node()
                curr=curr.one
    
    def findXOR(self,num):
        curr=self.root
        res=0
        for i in range(31,-1,-1):
            bit=(num>>i)&1
            if bit==0:
                if curr.one:
                    res+=(1<<i)
                    curr=curr.one
                else:
                    curr=curr.zero
            else:
                if curr.zero:
                    res+=(1<<i)
                    curr=curr.zero
                else:
                    curr=curr.one
        return res
class Solution:
    def maxXor(self, arr):
        #code here
        trie=Trie()
        result=0
        trie.insert(arr[0])
        for i in range(1,len(arr)):
            result=max(trie.findXOR(arr[i]),result)
            trie.insert(arr[i])
        return result'''

#Approach 3: Using Bit Manipulation
# We can also solve this problem using bit manipulation. The idea is to find the maximum xor possible by checking each bit from the most significant bit to the least significant bit.
# We will check if we can set the current bit in the result by checking if there is a pair of numbers which can give us that bit.
# If we can set the current bit in the result, we will set it and move to the next bit. Otherwise, we will move to the next bit without setting it.
class Solution:
    def maxXor(self, arr):
        #code here
        max_xor = 0
        for i in range(31, -1, -1):
            max_xor <<= 1   
            curr_xor = max_xor | 1
            found = False
            prefixes = set()
            for num in arr:
                prefixes.add(num >> i)
            for prefix in prefixes:
                if (prefix ^ curr_xor) in prefixes:
                    found = True
                    break
            if found:
                max_xor |= 1
        return max_xor
sol=Solution()
# print(sol.maxXor([25, 10, 2, 8, 5, 3])) #28
print(sol.maxXor([1, 2, 3, 4, 5, 6, 7])) #7