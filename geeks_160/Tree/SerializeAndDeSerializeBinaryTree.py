'''
Serialization is to store a tree in an array so that it can be later restored and deserialization is reading tree back from the array. Complete the functions

serialize() : stores the tree into an array a and returns the array.
deSerialize() : deserializes the array to the tree and returns the root of the tree.
Note: Multiple nodes can have the same data and the node values are always positive integers. Your code will be correct if the tree returned by deSerialize(serialize(input_tree)) is same as the input tree. Driver code will print the in-order traversal of the tree returned by deSerialize(serialize(input_tree)).

Examples :

Input: root = [1, 2, 3]
      
Output: [2, 1, 3]
Input: root = [10, 20, 30, 40, 60, N, N]
      
Output: [40, 20, 60, 10, 30]
Constraints:
1 <= Number of nodes <= 104
1 <= Data of a node <= 109
'''


class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        #code here
        list1=[]
        q=[root]
        while q:
            length=len(q)
            for i in range(length):
                curnode=q.pop(0)
                if curnode:
                    list1.append(curnode.data)
                    q.append(curnode.left)
                    q.append(curnode.right)
                else:
                    list1.append(curnode)
                
        return list1
        
        
    
    #Function to deserialize a list and construct the tree.   
    def deSerialize(self, arr):
        #code here
        if not arr or arr[0] is None:
            return None
            
        root=Node(arr[0])
        q=[root]
        i=1
        while q and i<len(arr):
            current=q.pop(0)
            if arr[i] is not None:
                current.left=Node(arr[i])
                q.append(current.left)
            i+=1
            if i<len(arr) and arr[i] is not None:
                current.right=Node(arr[i])
                q.append(current.right)
            i+=1
        return root