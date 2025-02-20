'''
Given an array arr[] of n sorted linked lists of different sizes. The task is to merge them in such a way that after merging they will be a single sorted linked list, then return the head of the merged linked list.

Examples:

Input: arr[] = [1 -> 2 -> 3, 4 -> 5, 5 -> 6, 7 -> 8]
Output: 1 -> 2 -> 3 -> 4 -> 5 -> 5 -> 6 -> 7 -> 8
Explanation:
The arr[] has 4 sorted linked list of size 3, 2, 2, 2.
1st list: 1 -> 2-> 3
2nd list: 4 -> 5
3rd list: 5 -> 6
4th list: 7 -> 8
The merged list will be:
 
Input: arr[] = [1 -> 3, 8, 4 -> 5 -> 6]
Output: 1 -> 3 -> 4 -> 5 -> 6 -> 8
Explanation:
The arr[] has 3 sorted linked list of size 2, 3, 1.
1st list: 1 -> 3
2nd list: 8
3rd list: 4 -> 5 -> 6
The merged list will be:

Constraints
1 <= total no. of nodes <= 105
1 <= node->data <= 103
'''

class Node:
    def _init_(self,x):
        self.data = x
        self.next = None

import heapq


class Solution:
    def mergeKLists(self, arr):
        # code here
        h=[]
        for head in arr:
            heapq.heappush(h,(head.data,head))
        finalhead=None
        prev=None
        while h:
            cur=heapq.heappop(h)
            head=cur[1]
            while head:
                if not finalhead:
                    finalhead=head
                if prev:
                    prev.next=head
                prev=head
                head=head.next
                if head and h:
                    if head.data>h[0][0]:
                        heapq.heappush(h,(head.data,head))
                        break
                    
        return finalhead
                
            
                
        # return head of merged list