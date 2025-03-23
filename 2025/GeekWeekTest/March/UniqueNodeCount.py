class Solution:
    # Function to find out the unique sizes for d days
    def uniqueSize(self, n, d, arr):
        # Code Here
        dict1=dict()
        dict1[0]=n
        nodes=[0]*n
        result=[]
        unique=1
        for node,length in arr:
            prev=nodes[node-1]
            nodes[node-1]+=length
            length=nodes[node-1]
            if prev in dict1:
                dict1[prev]-=1
                if dict1[prev]==0:
                    dict1.pop(prev)
                    unique-=1
            if length in dict1:
                dict1[length]+=1
            else:
                dict1[length]=1
                unique+=1
            result.append(unique)
        return result
sol=Solution()
n=3
d=4
# arr=[[1, 5],[2, 5],[1,10],[3,5]]
arr=[[2, 10],[3, 5],[1,5],[3,10]]
print(sol.uniqueSize(n,d,arr)) # Output: [2,2,3,2]