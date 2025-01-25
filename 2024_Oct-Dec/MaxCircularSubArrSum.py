def circularSubarraySum(arr):
    ##Your code here
    prev=0
    maxsofar=float('-inf')
    for num in arr:
        prev+=num
        if prev<num:
            prev=num
        maxsofar=max(maxsofar,prev)
    prefixsum=[]
    maxtill=[]
    max1=float('-inf')
    prev=0      
    for num in arr:
        prev+=num
        prefixsum.append(prev)
        max1=max(max1,prev)
        maxtill.append(max1)
    initmax=max(arr)
    finalmax=max(initmax,max(prefixsum),maxsofar)
    for i in range(1,len(arr)+1):
        right=prefixsum[-1]-prefixsum[i-1]
        left=maxtill[i-1]
        finalmax=max(finalmax,left+right)
    return finalmax


arrays=[
[8, -8, 9, -9, 10, -11,12],#22
        [10, -3, -4, 7, 6, 5, -4, -1],#23
        [-1, 40, -14, 7, 6, 5, -4, -1],#52
        [5, -2, 3, 4, 5],
        [3, -1, 2, -1],
        [3, -2, 2, -3],
        [-7, 32, -11, 21, 18, 35, -26, -17, 35, -12, -38, -33, 32, 16, 44, 11, -40, -21, 2, 27, -35, 21, -37, -12, 1]] #107

for arr in arrays:
    print(circularSubarraySum(arr))