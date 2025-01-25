class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def list_to_binary_tree(lst):
    if not lst:
        return None

    root = Node(lst[0])
    queue = [root]
    i = 1

    while i < len(lst):
        node = queue.pop(0)

        if lst[i] is not None:
            node.left = Node(lst[i])
            queue.append(node.left)
        i += 1

        if i < len(lst) and lst[i] is not None:
            node.right = Node(lst[i])
            queue.append(node.right)
        i += 1

    return root

def print_tree(root):
    if root:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)

lst = [49,45,1,20,46,15,39,27,None,None,None,25]
root = list_to_binary_tree(lst)

class Solution:
    def minimumOperations(self, root) -> int:
        swapcount = 0
        q = []
        q.append(root)
        while True:
            curlevel = []
            workinglist = []
            while q:
                cur = q.pop(0)
                if cur.left:
                    curlevel.append(cur.left)
                    workinglist.append(cur.left.val)
                if cur.right:
                    curlevel.append(cur.right)
                    workinglist.append(cur.right.val)
            if not curlevel:
                break
            pos = {val:index for index, val in enumerate(workinglist)}
            origlist=workinglist.copy()
            workinglist.sort()
            length = len(workinglist)
            j = length - 1
            while j >= 0:
                curmax = workinglist[j]
                if pos[curmax] == j:
                    j -= 1
                    continue
                else:
                    present=pos[curmax]
                    pos[curmax]=j
                    prev=origlist[j]
                    origlist[j]=curmax
                    origlist[present]=prev
                    pos[prev]=present
                    swapcount += 1
                j -= 1
            q = curlevel.copy()
        return swapcount
sol=Solution()
print(sol.minimumOperations(root))