'''
Kadane variation for multiplication type problem (maximum product subarray)
'''
class Solution:
	# Function to find maximum
	# product subarray
    def maxProduct(self, arr):
        n = len(arr)
        if n==1:
            return arr[0]
        # Variables to store maximum and minimum
        # product till ith index.
        max_ending = 0
        min_ending = 0
        max_so_far = 0
        # Traverse throughout the array
        for i in range(n):
            # If number is negative, swap maximum
            # and minimum product
            if arr[i] < 0:
                temp = max_ending
                max_ending = min_ending
                min_ending = temp
            # update maximum product ending at
            # current index
            max_ending = max(arr[i], max_ending * arr[i])
            # update minimum product ending at
            # current index
            min_ending = min(arr[i], min_ending * arr[i])
            # update maximum so far
            max_so_far = max(max_so_far, max_ending)
        # Return maximum product
        return max_so_far
                

sol=Solution()

arrs=[[-2, 6, -3, -10, 0, 2],
      [-1,-3,-10,0,60],
      [-2,-3,0,-2,-40],
      [-6],
      [0],
      [-1,0],
      [-1,-1],
      [-1,-1,-1],
      [0,0,-4],
      [0,0,-1,-4],
      [10, 4, 3, -7, -4, -5, 2]]
for arr in arrs:
    print(sol.maxProduct(arr))


