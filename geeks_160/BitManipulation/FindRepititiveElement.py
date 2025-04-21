'''
Given an array arr[] of size n, filled with numbers from 1 to n-1 in random order. The array has only one repetitive element. Your task is to find the repetitive element.

Note: It is guaranteed that there is a repeating element present in the array.

Examples:

Input: arr[] = [1, 3, 2, 3, 4]
Output: 3 
Explanation: The number 3 is the only repeating element.
Input: arr[] = [1, 5, 1, 2, 3, 4]
Output: 1  
Explanation: The number 1 is the only repeating element.
Input: arr[] = [1, 1]  
Output: 1
Explanation: The array is of size 2 with both elements being 1, making 1 the repeating element.
Constraints:
2 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ n-1 
'''
class Solution:
    def findDuplicate(self, arr):
        # XOR all elements in the array
        xor_all = 0
        for num in arr:
            xor_all ^= num
        
        # XOR with numbers from 1 to n-1
        n = len(arr)
        for i in range(1, n):
            xor_all ^= i
        
        # The result is the duplicate element
        return xor_all

# Example usage
sol = Solution()
print(sol.findDuplicate([1, 3, 2, 3, 4]))  # Output: 3
print(sol.findDuplicate([1, 5, 1, 2, 3, 4]))  # Output: 1
print(sol.findDuplicate([1, 1]))  # Output: 1

