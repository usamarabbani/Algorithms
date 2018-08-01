#find element in sorted matrix

def sortedMatrix(mat,size,x):
    i=0
    j=size-1
    while (i<size and j>=0):
        if (mat[i][j]==x):
            print("x found at ",i,"and",j)
            return 1
        if (mat[i][j]>x):
            j-=1
        else:
            i-=1



