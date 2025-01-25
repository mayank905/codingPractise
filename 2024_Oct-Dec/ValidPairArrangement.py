from collections import defaultdict


class Solution:
    def validArrangement(self, pairs):
        start=defaultdict(list)
        end=defaultdict(list)
        i=0
        for pair in pairs:
            start[pair[0]].append(i)
            end[pair[1]].append(i)
            i+=1
        
            


sol=Solution()
lists=[
    [[5,1],[4,5],[11,9],[9,4]],
    [[1,3],[3,2],[2,1]],
    [[1,2],[1,3],[2,1]]
]
for list in lists:
    print(sol.validArrangement(list))