#Input a Matrix, Check if do we get the same number consecutively
# at least 4 times in any fashion(Vertically, Horizontally, Diagonally).
# Record those sets.If we get multiple values, then print minimum of them.
#And if no such consecutive numbers then print -1.
#sample_input= 5
#              0 1 6 8 8 9
#              5 6 1 6 8 9
#              6 5 6 1 1 9
#              1 6 6 1 1 9
#              6 3 3 3 3 9

#sample_output= 1

row = int(input())
out_num = []
m = []

for i in range(row):
    row_no = list(map(int, input().split(" ")))
    m.append(row_no)

col = len(row_no)

for i in range(row):
    for j in range(col):

        if (j < col - 3):
            if (m[i][j] == m[i][j + 1] == m[i][j + 2] == m[i][j + 3]):
                out_num.append(m[i][j])

        if (i < row - 3):
            if (m[i][j] == m[i + 1][j] == m[i + 2][j] == m[i + 3][j]):
                out_num.append(m[i][j])

        if (j >= 3 and i <= 3):
            if (m[i][j] == m[i - 1][j - 1] == m[i - 2][j - 2] == m[i - 3][j - 3]):
                out_num.append(m[i][j])

        if (j < col - 3 and i >= 3):
            if (m[i][j] == m[i - 1][j + 1] == m[i - 2][j + 2] == m[i - 3][j + 3]):
                out_num.append(m[i][j])

if len(out_num) == 0:
    print(-1)
else:
    print(min(out_num))




#method2
row = int(input())
m = []

for i in range(row):
    row_no = list(map(int, input().split(" ")))
    m.append(row_no)

col = len(row_no)
res=[]
for i in range(row):
  for j in range(col-3):
    if(m[i][j]==m[i][j+1]==m[i][j+2]==m[i][j+3]):
      res.append(m[i][j])

for j in range(col):
  for i in range(row-3):
    if(m[i][j]==m[i+1][j]==m[i+2][j]==m[i+3][j]):
      res.append(m[i][j])

for i in range(row-3):
  for j in range(col-3):
    if(m[i][j]==m[i+1][j+1]==m[i+2][j+2]==m[i+3][j+3]):
      res.append(m[i][j])

for i in range(row-3):
  for j in range(col-3,col):
    if(m[i][j]==m[i-1][j-1]==m[i-2][j-2]==m[i-3][j-3]):
      res.append(m[i][j])

if(len(res)==0):
  print("-1")
else:
  res.sort()
  print(res[0])