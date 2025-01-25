'''
Given the head of two sorted linked lists consisting of nodes respectively. The task is to merge both lists and return the head of the sorted merged list.

Examples:

Input: head1 = 5 -> 10 -> 15 -> 40, head2 = 2 -> 3 -> 20
Output: 2 -> 3 -> 5 -> 10 -> 15 -> 20 -> 40
Explanation:

Input: head1 = 1 -> 1, head2 = 2 -> 4
Output: 1 -> 1 -> 2 -> 4
Explanation:

Constraints:
1 <= no. of nodes<= 103
0 <= node->data <= 105
'''
# Python3 program to merge two sorted linked lists

class Solution:
    def sortedMerge(self,head1, head2):
        # if both the lists are empty
        if head1 is None and head2 is None:
            return None
        # if first linked list is empty
        if head1 is None:
            return head2
        # if second linked list is empty
        if head2 is None:
            return head1
        # if both lists are non-empty
        if head1.data < head2.data:
            head1.next = self.sortedMerge(head1.next, head2)
            return head1
        else:
            head2.next = self.sortedMerge(head1, head2.next)
            return head2
