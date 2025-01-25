def maximize_mana(arr, k):
    n = len(arr)
    dp = [[0] * 2 for _ in range(n)]
    
    # Initial state
    dp[0][0] = arr[0] - k  # Using Purification Spell on the first door
    dp[0][1] = arr[0]      # Using Shadow Spell on the first door

    for i in range(1, n):
        # Using Purification Spell on the i-th door
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + arr[i] - k
        
        # Using Shadow Spell on the i-th door
        dp[i][1] = dp[i-1][0] + arr[i] // 2

    return max(dp[n-1][0], dp[n-1][1])

# Example usage
arr1 = [3, 6, 9, 2]
k1 = 4
print(maximize_mana(arr1, k1))  # Output: 7

arr2 = [2, 1, 6, 10]
k2 = 1
print(maximize_mana(arr2, k2))  # Output: 15