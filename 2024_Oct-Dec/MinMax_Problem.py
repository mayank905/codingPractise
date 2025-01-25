
def aggressiveCows(self, stalls, k):
    def can_place_cows(stalls, k, min_dist):
        count = 1
        last_position = stalls[0]
        
        for i in range(1, len(stalls)):
            if stalls[i] - last_position >= min_dist:
                count += 1
                last_position = stalls[i]
                if count == k:
                    return True
        return False
    stalls.sort()
    low = 1
    high = stalls[-1] - stalls[0]
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        if can_place_cows(stalls, k, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return result
