'''
Design a data structure that works like a LRU Cache. Here cap denotes the capacity of the cache and Q denotes the number of queries. Query can be of two types:

PUT x y: sets the value of the key x with value y
GET x: gets the key of x if present else returns -1.
The LRUCache class has two methods get() and put() which are defined as follows.

get(key): returns the value of the key if it already exists in the cache otherwise returns -1.
put(key, value): if the key is already present, update its value. If not present, add the key-value pair to the cache. If the cache reaches its capacity it should remove the least recently used item before inserting the new item.
In the constructor of the class the capacity of the cache should be initialized.
Examples:

Input: cap = 2, Q = 2, Queries = [["PUT", 1, 2], ["GET", 1]]
Output: [2]
Explanation: Cache Size = 2
["PUT", 1, 2] will insert the key-value pair (1, 2) in the cache,
["GET", 1] will print the value corresponding to Key 1, ie 2.
Input: cap = 2, Q = 8, Queries = [["PUT", 1, 2], ["PUT", 2, 3], ["PUT", 1, 5], ["PUT", 4, 5], ["PUT", 6, 7], ["GET", 4], ["PUT", 1, 2], ["GET", 3]]
Output: [5, -1]
Explanation: Cache Size = 2
["PUT", 1, 2] will insert the pair (1,2) in the cache.
["PUT", 2, 3] will insert the pair (2,3) in the cache: 1->2, 2->3(the most recently used one is kept at the rightmost position) 
["PUT", 1, 5] will replace the value of 1 from 2 to 5 : 2 -> 3, 1 -> 5
["PUT", 4, 5] : 1 -> 5, 4 -> 5 (Cache size is 2, hence we delete the least recently used key-value pair)
["PUT", 6, 7] : 4 -> 5, 6 -> 7 
["GET", 4] : Prints 5 (The cache now looks like 6 -> 7, 4->5)
["PUT", 1, 2] : 4 -> 5, 1 -> 2  (Cache size is 2, hence we delete the least recently used key-value pair)
["GET", 3] : No key value pair having key = 3. Hence, -1 is printed.
Constraints:
1 <= cap <= 103
1 <= Q <= 105
1 <= x, y <= 104
'''
from collections import deque

class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self, cap):
        #code here
        self.cap=cap
        self.dict1=dict()
        self.que=deque()
        self.itemCount=0
        
    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
        if key in self.dict1:
            self.que.remove(key)
            self.que.append(key)
            return self.dict1[key]
        else:
            return -1
        
    #Function for storing key-value pair.   
    def put(self, key, value):
        #code here
        if key in self.dict1:
            self.dict1[key]=value
            self.que.remove(key)
            self.que.append(key)
        else:
            if self.itemCount<self.cap:
                self.dict1[key]=value
                self.itemCount+=1
                self.que.append(key)
            else:
                item=self.que.popleft()
                del self.dict1[item]
                self.dict1[key]=value
                self.que.append(key)
sol=LRUCache(2)
queries = [
    ("PUT", 97, 30), ("GET", 43), ("GET", 13), ("PUT", 48, 56), ("GET", 67), ("GET", 60),
    ("PUT", 74, 43), ("PUT", 72, 39), ("PUT", 100, 59), ("GET", 85), ("PUT", 91, 62),
    ("GET", 72), ("PUT", 1, 4), ("GET", 1), ("GET", 53), ("GET", 5), ("PUT", 59, 60),
    ("PUT", 18, 95), ("GET", 37), ("GET", 61), ("GET", 15), ("PUT", 66, 38), ("GET", 22),
    ("GET", 10), ("PUT", 33, 1), ("GET", 5), ("PUT", 57, 59), ("PUT", 69, 11), ("PUT", 29, 70),
    ("PUT", 75, 47), ("GET", 6), ("GET", 2), ("PUT", 68, 90), ("GET", 27), ("GET", 39),
    ("PUT", 1, 6), ("GET", 58), ("GET", 49), ("PUT", 8, 18), ("PUT", 70, 98), ("GET", 29),
    ("PUT", 71, 19), ("PUT", 81, 93), ("GET", 55), ("PUT", 44, 8), ("GET", 51), ("PUT", 89, 86),
    ("GET", 91), ("GET", 35), ("PUT", 84, 26), ("PUT", 43, 95), ("GET", 92), ("PUT", 21, 21),
    ("GET", 39), ("GET", 93), ("GET", 23), ("GET", 86), ("GET", 95), ("GET", 9), ("GET", 3),
    ("PUT", 23, 85), ("PUT", 58, 26), ("PUT", 93, 3), ("GET", 97), ("GET", 31), ("GET", 50),
    ("PUT", 57, 13), ("PUT", 49, 55), ("GET", 29), ("GET", 58), ("GET", 77), ("PUT", 21, 98),
    ("PUT", 6, 95), ("GET", 83), ("GET", 24), ("PUT", 16, 37), ("PUT", 54, 85), ("PUT", 55, 25),
    ("GET", 37), ("GET", 93), ("GET", 59), ("GET", 24)
]
for query in queries:
    if query[0] == "PUT":
        sol.put(query[1], query[2])
    elif query[0] == "GET":
        print(sol.get(query[1]))