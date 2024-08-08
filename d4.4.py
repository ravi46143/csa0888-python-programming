# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:57:48 2024

@author: Rajesh
"""

s=input()
list1=[]
for i in s:
    list1+=i
print(list1)
m=sorted(list1)
m.reverse()
print(m)