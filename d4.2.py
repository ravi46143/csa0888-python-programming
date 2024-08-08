# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:36:01 2024

@author: Rajesh
"""

n=int(input())
s=input().split(' ')
list1=[]
for char in s:
    i=int(char)
    list1.append(i)
set1=set(list1)
p=sorted(list(set1))
l=max(p)
r=p[:len(p)-1]
print(max(r))