'''
There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

Example 1:

Input: colors = [0,1,0,1,0], k = 3

Output: 3

Explanation:



Alternating groups:



Example 2:

Input: colors = [0,1,0,0,1,0,1], k = 6

Output: 2

Explanation:



Alternating groups:



Example 3:

Input: colors = [1,1,0,1], k = 4

Output: 0

Explanation:



 

Constraints:

3 <= colors.length <= 105
0 <= colors[i] <= 1
3 <= k <= colors.length
'''
from typing import List
class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        length = len(colors)
        result = 0
        # Tracks the length of the current alternating sequence
        alternating_elements_count = 1
        last_color = colors[0]

        # First pass through the array
        for index in range(1, length):
            # Check if the current color is the same as the last one
            if colors[index] == last_color:
                # Pattern breaks, reset sequence length
                alternating_elements_count = 1
                last_color = colors[index]
                continue

            # Sequence can be extended
            alternating_elements_count += 1

            # If sequence length reaches at least k, count it
            if alternating_elements_count >= k:
                result += 1

            last_color = colors[index]

        # Wrap around to the first k - 1 elements
        for index in range(k - 1):

            # Pattern breaks. Since there are less than k elements remaining,
            # no more sequences can be formed
            if colors[index] == last_color:
                break

            # Extend the pattern
            alternating_elements_count += 1

            # Record a new alternating sequence
            if alternating_elements_count >= k:
                result += 1

            last_color = colors[index]

        return result
sol=Solution()
colors=[0,1,0,1,0]
k=3
colors=[0,1,0,0,1,0,1]
k=6
print(sol.numberOfAlternatingGroups(colors,k))