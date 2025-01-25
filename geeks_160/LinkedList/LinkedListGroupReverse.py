'''
Given the head a linked list, the task is to reverse every k node in the linked list. If the number of nodes is not a multiple of k then the left-out nodes in the end, should be considered as a group and must be reversed.

Examples:

Input: head = 1 -> 2 -> 2 -> 4 -> 5 -> 6 -> 7 -> 8, k = 4
Output: 4 -> 2 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5

Explanation: The first 4 elements 1, 2, 2, 4 are reversed first and then the next 4 elements 5, 6, 7, 8. Hence, the resultant linked list is 4 -> 2 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5.
Input: head = 1 -> 2 -> 3 -> 4 -> 5, k = 3
Output: 3 -> 2 -> 1 -> 5 -> 4

Explanation: The first 3 elements 1, 2, 3 are reversed first and then left out elements 4, 5 are reversed. Hence, the resultant linked list is 3 -> 2 -> 1 -> 5 -> 4.
Constraints:
1 <= size of linked list <= 105
1 <= data of nodes <= 106
1 <= k <= size of linked list
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
          
class Solution:
    def reverseKGroup(self, head, k):
        def minreverse(grp, prev, head):
            while grp != 0 and head is not None:
                cur = head
                head = head.next
                cur.next = prev
                prev = cur
                grp -= 1
            return prev, head
            
        bol = True
        newstart = None
        newend=head
        while head:
            grp = k
            anotherhead=head
            if bol:
                newstart, head = minreverse(grp, None, head)
                bol = False
            else:
                newend.next, head = minreverse(grp, None, head)
                newend=anotherhead

        return newstart

sol = Solution()
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)
head.next.next.next.next.next.next.next.next.next = Node(10)
k = 4
head=sol.reverseKGroup(head, k)
while head:
    print(head.data, end=" ")
    head = head.next
