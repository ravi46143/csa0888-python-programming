
def gcd1(a,b):
    while(b!=0):
        temp=b
        b=a%b
        a=temp
    return a

n=int(input())
a=int(input())
b=int(input())
result=gcd1(a,b)
print(result)
lcm=(a*b)//result
print(lcm)