# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:22:50 2024

@author: Rajesh
"""

p=[26, 28, 47, 26, 43, 51, 29]
row=[]
for i in range(len(p)):
    count=0
    for j in range(1,p[i]):
        if p[i]%j==0:
            count+=1
    if count<2:
            row+=[p[i]]
print(row)
            