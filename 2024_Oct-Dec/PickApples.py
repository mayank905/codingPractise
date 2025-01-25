class Solution:
    
    def manhattanDist(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    

    def solve(self, points, a, b, i, memo):
        

        if i == len(points):
            return 0

        if memo[a][b] != -1:
            return memo[a][b]
        

        d1 = self.manhattanDist(points[a], points[i]) + self.solve(points, i, b, i + 1, memo)
        

        d2 = self.manhattanDist(points[b], points[i]) + self.solve(points, a, i, i + 1, memo)
        
        memo[a][b] = min(d1, d2)
        return min(d1, d2)
        
    def minDistance(self, alice, bob, apples):
        points = []
        points.append(alice)
        points.append(bob)
        
        for apple in apples:
            points.append(apple)
        
        memo = [[-1 for _ in range(len(points))] for _ in range(len(points))]
        
        return self.solve(points, 0, 1, 2, memo)
sol=Solution()
alice=[5, 8]
bob=[1, 7]
apples=[[9, 7],
[-2, 9],
[10, 0],
[6, 8],
[2, -3],
[3, -4],
[-2, 0],
[10, 8],
[2, 7],
[9, 6],
[8, 6],
[3 ,10],
[4 ,5],
[2, 0],
[-1 ,-3],
[9 ,-1],
[5 ,6],
[5, 3],
[3,-4],
[7, -4]]
print(sol.minDistance(alice,bob,apples))
'''
20
5 8
1 7
9 7
-2 9
10 0
6 8
2 -3
3 -4
-2 0
10 8
2 7
9 6
8 6
3 10
4 5
2 0
-1 -3
9 -1
5 6
5 3
3 -4
7 -4

output 122
'''