# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 12:59:27 2024

@author: Rajesh
"""

def fact(n):
    f=1
    for i in  range(1,n+1):
        f=f*i
    return f
n=int(input())
resutl=fact(n)
print(resutl)