'''
class Node:  
    def __init__(self, val):  
        self.data = val  
        self.left = None  
        self.right = None 
'''
from asyncio import Queue


class Solution:  
    def differenceSum(self, root1, root2):  
        # write your code here
        def bfs_sum(tree1, tree2):
            queue1 = [tree1] if tree1 else []
            queue2 = [tree2] if tree2 else []
            diff_sum = 0
            
            while queue1 or queue2:
                node1 = queue1.pop(0) if queue1 else None
                node2 = queue2.pop(0) if queue2 else None
                
                # Calculate the absolute difference and add to the sum
                val1 = node1.data if node1 else 0
                val2 = node2.data if node2 else 0
                diff_sum += abs(val1 - val2)
                
                # Traverse left and right children if they exist
                if node1:
                    queue1.extend([node1.left, node1.right])
                if node2:
                    queue2.extend([node2.left, node2.right])

            return diff_sum
    
        return bfs_sum(root1, root2)
        
        

#{ 
 # Driver Code Starts.
class Node:  
    def __init__(self, val):  
        self.data = val  
        self.left = None  
        self.right = None  


def input_tree(n,arr):  
    n = n 
    if n == 0:  
        return None  
    
    ar = arr  
    root = Node(ar[0])  
    queue = Queue()  
    queue.put(root)  # enqueue the root node
    i = 1  

    while i < n:  
        curr = queue.get()  # dequeue from the front
        if i < n:  
            curr.left = Node(ar[i])  
            queue.put(curr.left)  # enqueue the left child
            i += 1  
        if i < n:  
            curr.right = Node(ar[i])  
            queue.put(curr.right)  # enqueue the right child
            i += 1  

    return root  

if __name__ == "__main__":    
    n1=9
    arr1=[-17, 82, 52, 70, 80, -100, 37, 6, 92]
    n2=4
    arr2=[17, -70, -3, 29]
    root1 = input_tree(n1,arr1)  
    root2 = input_tree(n2,arr2)  

    obj = Solution()  
    res = obj.differenceSum(root1, root2)  

    print(res)
    print("~")
# } Driver Code Ends
