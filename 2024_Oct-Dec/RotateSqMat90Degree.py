def newIndex(base,row,col,length):
    step=length-1
    if row==base and col<step:
        diff=(col-base)%step
        row+=diff
        col=step
        return [row,col]
    if row<step and col==step:
        diff=(row-base)%step
        col-=diff
        row=step
        return [row,col]
    if row==step and col>base:
        diff=(step-col)%step
        col=base
        row-=diff
        return [row,col]
    if row>base and col==base:
        diff=(step-row)%step
        col+=diff
        row=base
        return [row,col]


def rotateOuterMat(index,length,mat):
    for i in range(index,index+length-1):
        startingIndex=[index,i]
        curValue=mat[startingIndex[0]][startingIndex[1]]
        for j in range(4):            
            newInd=newIndex(index,startingIndex[0],startingIndex[1],index+length)
            temp=mat[newInd[0]][newInd[1]]
            mat[newInd[0]][newInd[1]]=curValue
            curValue=temp
            startingIndex[0]=newInd[0]
            startingIndex[1]=newInd[1]



def rotate(mat): 
    length=len(mat)
    origLength=length
    while length>1:
        index=(origLength-length)//2
        rotateOuterMat(index,length,mat)
        length-=2


# mat = [[1,2,3], [4, 5, 6], [7, 8, 9]]
# mat = [[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,16]]
mat=[[1, 2], [3, 4]]
rotate(mat)
N=len(mat)
for i in range(N):
    for j in range(N):
        print(mat[i][j], end=' ')
    print()
print("~")



'''
Given a square mat[][]. The task is to rotate it by 90 degrees in clockwise direction without using any extra space.
'''