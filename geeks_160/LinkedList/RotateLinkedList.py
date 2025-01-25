'''
Given the head of a singly linked list, your task is to left rotate the linked list k times.

Examples:

Input: head = 10 -> 20 -> 30 -> 40 -> 50, k = 4
Output: 50 -> 10 -> 20 -> 30 -> 40
Explanation:
Rotate 1: 20 -> 30 -> 40 -> 50 -> 10
Rotate 2: 30 -> 40 -> 50 -> 10 -> 20
Rotate 3: 40 -> 50 -> 10 -> 20 -> 30
Rotate 4: 50 -> 10 -> 20 -> 30 -> 40

Input: head = 10 -> 20 -> 30 -> 40 , k = 6
Output: 30 -> 40 -> 10 -> 20 
 
Constraints:

1 <= number of nodes <= 105
0 <= k <= 109
0 <= data of node <= 109
'''

class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        cur=head
        length=0
        prev=None
        while cur!=None:
            prev=cur
            cur=cur.next
            length+=1
        k%=length
        last=prev
        prev.next=head
        while k!=0:
            last=head
            head=head.next
            k-=1
        last.next=None
        return head