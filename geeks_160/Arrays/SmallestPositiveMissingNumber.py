'''
You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.

Note: Positive number starts from 1. The array can have negative integers too.

Examples:

Input: arr[] = [2, -3, 4, 1, 1, 7]
Output: 3
Explanation: Smallest positive missing number is 3.
Input: arr[] = [5, 3, 2, 5, 1]
Output: 4
Explanation: Smallest positive missing number is 4.
Input: arr[] = [-8, 0, -1, -4, -3]
Output: 1
Explanation: Smallest positive missing number is 1.
Constraints:  
1 <= arr.size() <= 105
-106 <= arr[i] <= 106
'''
class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        class MyClass:
            def __init__(self, value):
                self.value = value
        dict1=dict()
        smallest=1
        for num in arr:
            if num<=0:
                continue
            else:
                if num not in dict1:
                    dict1[num]=MyClass(num+1)
                if num-1 in dict1:
                    dict1[num-1].value=dict1[num].value
                    dict1[num]=dict1[num-1]
                if num+1 in dict1:
                    dict1[num].value=dict1[num+1].value
                    dict1[num+1]=dict1[num]
                
        if smallest in dict1:
            return dict1[smallest].value
        else:
            return smallest