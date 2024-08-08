n=[[1,2,3],[4,5,6],[7,8,9]]
m=[[9,8,7],[6,5,4],[3,2,1]]
s=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        for k in range(3):
            s[i][j]+=n[i][k]*m[k][j]
print(s)
