'''
Given the head of two singly linked lists num1 and num2 representing two non-negative integers. The task is to return the head of the linked list representing the sum of these two numbers.

For example, num1 represented by the linked list : 1 -> 9 -> 0, similarly num2 represented by the linked list: 2 -> 5. Sum of these two numbers is represented by 2 -> 1 -> 5.

Note: There can be leading zeros in the input lists, but there should not be any leading zeros in the output list.

Examples:

Input: num1 = 4 - > 5, num2 = 3 -> 4 -> 5
Output:  3 -> 9 -> 0
 
Explanation: Given numbers are 45 and 345. There sum is 390.
Input: num1 = 0 -> 0 -> 6 -> 3, num2 = 0 -> 7 
Output: 7 -> 0 
 
Explanation: Given numbers are 63 and 7. There sum is 70.
Constraints:
1 <= size of both linked lists <= 106
0 <= elements of both linked lists <= 9
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    def addTwoLists(self, num1, num2):
        # code here
        def removeZero(head):
            while head and head.data==0:
                head=head.next
            return head
        def reverselist(head):
            prev=None
            length=0
            while head:
                length+=1
                cur=head
                head=head.next
                cur.next=prev
                prev=cur
            return prev,length
        list1,length1=reverselist(num1)
        list2,length2=reverselist(num2)
        if length1>length2:
            temp=list1
            list1=list2
            list2=temp
        carry=0
        laterUse=list2
        while list2:
            data2=list2.data
            data1=list1.data if list1 else 0
            newdata=data1+data2+carry
            carry=newdata//10
            newdata%=10
            list2.data=newdata
            list2=list2.next
            if list1:
                list1=list1.next
        newhead,length=reverselist(laterUse)
        if carry!=0:
            newNode=Node(carry)
            newNode.next=newhead
            return removeZero(newNode)
        return removeZero(newhead)
sol = Solution()
num1 = Node(0)
num1.next = Node(0)
num1.next.next = Node(6)
num1.next.next.next = Node(3)
num2 = Node(0)
num2.next = Node(7)
# num2.next.next = Node(8)
# num2.next.next.next = Node(9)
# num2.next.next.next.next = Node(1)
# num2.next.next.next.next.next = Node(2)
# num2.next.next.next.next.next.next = Node(3)
# num2.next.next.next.next.next.next.next = Node(4)
# num2.next.next.next.next.next.next.next.next = Node(5)
newhead=sol.addTwoLists(num1, num2)
while newhead:
    print(newhead.data,end=' ')
    newhead=newhead.next
