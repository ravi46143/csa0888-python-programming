# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:20:25 2024

@author: Rajesh
"""

n=int(input())
digit=""
for i in range(n):
    s=int(input())
    digit+=str(s)
d=int(digit)
sum1=0
while(d!=0):
    a=d%10
    sum1+=a
    d//=10
print("sum=",sum1)