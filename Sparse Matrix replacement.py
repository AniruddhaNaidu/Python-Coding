row_no=int(input())
inmatrix=[]
for i in range(row_no):
    row=list(map(int,input().strip().split(" ")))
    inmatrix.append(row)
col_no=len(inmatrix[0])

def sparse_check(mat,row_no,col_no):
    counter=0
    for i in range(row_no):
        for j in range(0,col_no):
            if mat[i][j]==0:
                counter+=1

    if counter>=((row_no*col_no)/2):
        return 1
    else:
        return 0

def elemsum(mat,it,v):

    rowsum = 0
    rowsum += sum(mat[it])
    colsum = 0
    for j in range(row_no):
        colsum += mat[j][v]
    return rowsum,colsum



if(sparse_check(inmatrix,row_no,col_no)):
    for i in range(row_no):
        for v in range(0, col_no):
            rowsum,colsum=elemsum(inmatrix,i,v)
            print(rowsum)
            print(colsum)
            if rowsum<=colsum:
                if inmatrix[i][v] == 0:
                    for x in range(0,3):
                        if (rowsum+x)%2==0:
                            num=x
                            inmatrix[i][v]=num
                            break


            else:

                if inmatrix[i][v] == 0:
                    for x in range(0,4):
                        if (rowsum+x)%3==0:
                            num=x
                            inmatrix[i][v]=num
                            break


    print(inmatrix)

else:
    print(-1)




