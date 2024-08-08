# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 08:15:37 2024

@author: Rajesh
"""
#method one
list1=[1,3,5,3,7,1,9,3]
list1.reverse()
print(list1)
#method two
list1=[1,2,3,4,5,6]
print(list1[::-1])
#method three
list1=[1,2,3,4,4,5,6,7]
p=len(list1)
list2=[]
for i in range(p-1,-1,-1):
    list2.append(list1[i])
print(list2)