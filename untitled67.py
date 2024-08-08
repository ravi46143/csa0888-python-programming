# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 08:17:32 2024

@author: Rajesh
"""

list1=[9,8,7,0]
list2=[3,4,5,6]
list1.extend(list2)
print(sorted(list1))

p=[9,8,7,0]
q=[3,4,5,6]
c=p+q
print("before sort:")
print(c)
for i in range(len(c)):
    for j in range(0,len(c)):
        if c[i]<c[j]:
            temp=c[i]
            c[i]=c[j]
            c[j]=temp
print("after the  sorting")
print(c)