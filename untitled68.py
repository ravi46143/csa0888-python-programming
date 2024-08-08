# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 08:23:19 2024

@author: Rajesh
"""
list1=[1,2,3,4,5,6,7,8,9]
e_count=0
o_count=0
for i in range(1,len(list1)+1):
    if i%2==0:
        e_count+=1
    else:
        o_count+=1
print("even number=",e_count)
print("odd number=",o_count)
        
        