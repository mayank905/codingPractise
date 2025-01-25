from collections import defaultdict
class Solution:
    def isPossible(self, n, conditions):
        # code here
        events = []
        for l, r, x in conditions:
            if l<0 or r>=n:
                return False
            for bit in range(30):  
                if x & (1 << bit):  
                    events.append((l, bit, 1)) 
                    events.append((r + 1, bit, -1))  

        events.sort()


        active_bits = defaultdict(int)
        bit_set_by_index = [0] * n 

        prev_index = 0
        for index, bit, change in events:
            for i in range(prev_index, min(index, n)):
                for b, count in active_bits.items():
                    if count > 0: 
                        bit_set_by_index[i] |= (1 << b)

            active_bits[bit] += change

            prev_index = index

        for l, r, x in conditions:
            bitwise_and = bit_set_by_index[l]
            for i in range(l + 1, r + 1):
                bitwise_and &= bit_set_by_index[i]
            if bitwise_and != x:
                return False

        return True

sol=Solution()
n=5
conditions=[[0, 5, 2], [0, 5, 6]]

print(sol.isPossible(n,conditions))