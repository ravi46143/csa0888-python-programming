# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:02:43 2024

@author: Rajesh
"""

list_a=[1,23,45,231,335]
n=int(input())
if n<=0 or n>len(list_a):
    print("n valide")
else:
    sort=sorted(list_a,reverse=True)
    largest=sort[n-1]
    print(largest)