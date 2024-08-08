n=input()
s=int(n)
leng=len(n)
if leng%2==0:
     half=leng//2
     first=int(n[:half])
     seconf=int(n[half:])
     sum1=first+seconf
     sum1=sum1**2
     if sum1==s:
          print("tech number")
     else:
        print("not tech number")
else:
    print("enter the even length number")
