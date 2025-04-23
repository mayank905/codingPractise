'''
Given an array arr[] containing 2*n + 2 positive numbers, out of which 2*n numbers exist in pairs whereas the other two number occur exactly once and are distinct. Find the other two numbers. Return the answer in increasing order.

Examples:

Input: arr[] = [1, 2, 3, 2, 1, 4]
Output: [3, 4] 
Explanation: 3 and 4 occur exactly once.
Input: arr[] = [2, 1, 3, 2]
Output: [1, 3]
Explanation: 1 and 3 occur exactly once.
Input: arr[] = [2, 1, 3, 3]
Output: [1, 2]
Explanation: 1 and 2 occur exactly once.
Constraints:
2 ≤ arr.size() ≤ 106 
1 ≤ arr[i] ≤ 5 * 106
arr.size() is even
'''

class Solution:
    def singleNum(self, arr):
        # Code here
        # Find the XOR of all elements in the array
        xor = 0
        for num in arr:
            xor ^= num
    

        # Find the rightmost set bit in xor
        set_bit = xor & -xor
        #print binary representation of xor and -xor
        print(bin(xor), bin(-xor))
        #print binary representation of set_bit
        print(bin(set_bit))

        # Initialize the two unique numbers to 0
        num1 = 0
        num2 = 0

        # Divide the elements into two groups based on the set bit
        for num in arr:
            if num & set_bit:
                num1 ^= num  # XOR of first group
            else:
                num2 ^= num  # XOR of second group  

        # Return the two unique numbers in increasing order
        return [min(num1, num2), max(num1, num2)]

sol=Solution()
# arr=[1, 2, 3, 2, 1, 4]
# print(sol.singleNum(arr)) #Output: [3, 4]
# arr=[2, 1, 3, 2]
# print(sol.singleNum(arr)) #Output: [1, 3]
arr=[2, 1, 3, 3]
print(sol.singleNum(arr)) #Output: [1, 2]