n=int(input("enter the number:"))
sum1=0
temp=n
while(n>0):
    a=n%10
    c=a**3
    sum1+=c
    n//=10
if temp==sum1:
    print("armstrong number")
else:
    print("not a armstrong number")