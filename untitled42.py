# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 12:12:18 2024

@author: Rajesh
"""
p=[14,62,16,23,48,5,69]
a=sorted(p)

b=a[::-1]
n=int(input())
m=int(input())
print("min=",a[n-1])
print("max=",b[m-1])
print(a[n-1]+b[m-1])
print(a[n-1]-b[m-1])
print(a[n-1]*b[m-1])