# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:42:49 2024

@author: Rajesh
"""



def sumofsquare(list1):
    sum1=0
    sum2=0
    new=[]
    for i in list1:
        if i%2 == 0:
            sum1+=(i**2)
        
        else:
            sum2+=(i**2)
    new.append(sum2)
    new.append(sum1)
    return new
n=int(input())
list1=[]
for i in range(n):
    s=int(input())
    list1.append(s)
result=sumofsquare(list1)
print(result)