n=int(input())

for i in range(1,n+1):
    k=0.1
    for j in range(1,i):
        print(str(round(k,1))+" ",end="")
        k=k+0.1
    print()
   