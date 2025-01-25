'''
You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.

 

Example 1:

Input: boxes = "110"
Output: [1,1,3]
Explanation: The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
Example 2:

Input: boxes = "001011"
Output: [11,8,5,4,3,4]
 

Constraints:

n == boxes.length
1 <= n <= 2000
boxes[i] is either '0' or '1'.
'''
from typing import List

'''
The idea is to calculate the number of operations needed to move all the balls to the ith box.
For each box, we calculate the number of operations needed to move all the balls to the ith box.
Better Solution:
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        balls_to_left = 0
        moves_to_left = 0
        balls_to_right = 0
        moves_to_right = 0

        # Single pass: calculate moves from both left and right
        for i in range(n):
            # Left pass
            answer[i] += moves_to_left
            balls_to_left += int(boxes[i])
            moves_to_left += balls_to_left

            # Right pass
            j = n - 1 - i
            answer[j] += moves_to_right
            balls_to_right += int(boxes[j])
            moves_to_right += balls_to_right

        return answer
'''
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        i=0
        length=len(boxes)
        indices=[]
        for i in range(length):
            if boxes[i]=='1':
                indices.append((i,length-1-i))
        left=0
        right=0
        for index in indices:
            left+=index[0]
            # right+=index[1]
        leftindlength=len(indices)
        rightindlength=0
        result=[]
        for i in range(length):
            temp1=max(0,(left-(i*leftindlength)))
            temp2=max(0,right-((length-1-i)*rightindlength))
            temp=temp1+temp2
            if boxes[i]=='1':
                left-=indices[0][0]
                right+=indices[0][1]
                indices.pop(0)
                leftindlength-=1
                rightindlength+=1
            result.append(abs(temp))
        return result
sol=Solution()
boxes="110"
# boxes="001011"
print(sol.minOperations(boxes))