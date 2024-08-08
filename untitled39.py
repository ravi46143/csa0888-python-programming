# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:16:48 2024

@author: Rajesh
"""

list_a=[16, 18, 27, 16, 23, 21, 19]
c_count=0
for i in range(len(list_a)):
    count=0
    for j in range(1,list_a[i]):
        if list_a[i]%j==0:
            count+=1
    if count>2:
        c_count+=1
print(c_count)
            