# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 09:54:39 2024

@author: Rajesh
"""
def prime(num,div=None):
    if num<=1:
        return False
    if div is None:
        div=num-1
    if div==1:
        return True
    if num%div==0:
        return False
    return prime(num,div-1)



num=int(input())
if prime(num): 
    print("prime number")
else:
    print("not prime number")