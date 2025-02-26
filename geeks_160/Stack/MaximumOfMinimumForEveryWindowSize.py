'''
Given an array of integers arr[], the task is to find the maximum of the minimum values for every possible window size in the array, where the window size ranges from 1 to arr.size().

More formally, for each window size k, determine the smallest element in all windows of size k, and then find the largest value among these minimums where 1<=k<=arr.size().

Examples :

Input: arr[] = [10, 20, 30, 50, 10, 70, 30]
Output: [70, 30, 20, 10, 10, 10, 10] 
Explanation: 
1. First element in output indicates maximum of minimums of all windows of size 1. Minimums of windows of size 1 are [10], [20], [30], [50], [10], [70] and [30]. Maximum of these minimums is 70. 
2. Second element in output indicates maximum of minimums of all windows of size 2. Minimums of windows of size 2 are [10], [20], [30], [10], [10], and [30]. Maximum of these minimums is 30. 
3. Third element in output indicates maximum of minimums of all windows of size 3. Minimums of windows of size 3 are [10], [20], [10], [10] and [10]. Maximum of these minimums is 20. 
Similarly other elements of output are computed.
Input: arr[] = [10, 20, 30]
Output: [30, 20, 10]
Explanation: First element in output indicates maximum of minimums of all windows of size 1. Minimums of windows of size 1 are [10] , [20] , [30]. Maximum of these minimums are 30 and similarly other outputs can be computed
Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <= 106
'''

def maxOfMin(arr):
    n = len(arr)
    
    # Arrays to store previous and next smaller elements
    prev_smaller = [-1] * n
    next_smaller = [n] * n
    
    # Stack to find previous and next smaller elements
    stack = []
    
    # Fill entries in prev_smaller[]
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            prev_smaller[i] = stack[-1]
        stack.append(i)
    
    # Clear the stack for next use
    stack = []
    
    # Fill entries in next_smaller[]
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            next_smaller[i] = stack[-1]
        stack.append(i)
    
    # Initialize the result array
    result = [0] * (n + 1)
    
    # Fill the result array using prev_smaller[] and next_smaller[]
    for i in range(n):
        length = next_smaller[i] - prev_smaller[i] - 1
        result[length] = max(result[length], arr[i])
    
    # Fill the remaining entries in result[]
    for i in range(n - 1, 0, -1):
        result[i] = max(result[i], result[i + 1])
    
    # Remove the extra element at the beginning
    return result[1:]

# Example usage
arr1 = [10, 20, 30, 50, 10, 70, 30]
print(maxOfMin(arr1))  # Output: [70, 30, 20, 10, 10, 10, 10]

arr2 = [10, 20, 30]
print(maxOfMin(arr2))  # Output: [30, 20, 10]
