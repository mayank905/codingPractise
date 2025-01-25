from collections import Counter
class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        length=len(arr)
        onethird=length//3
        C=Counter(arr)
        result=[]
        C=C.most_common()
        for item in C:
            if item[1]>onethird:
                result.append(item[0])
        result=sorted(result)
        return result
if __name__ == '__main__':
    sol=Solution()
    with open('fileInput3.txt', 'r') as file:
        arr = list(map(int, file.read().split()))

    print(sol.findMajority(arr)) 