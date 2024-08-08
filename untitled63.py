# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 09:48:18 2024

@author: Rajesh
"""
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input())
result=factorial(n)
print(result)