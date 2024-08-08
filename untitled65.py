# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:10:53 2024

@author: Rajesh
"""
n=int(input())
if n>=90:
    print("S grade")
elif n>=80 and n<=89:
    print("A grade")
elif n>=70 and n<=79:
    print("B grade")
elif n>=60 and n<=69:
    print("C grade")
elif n>=50 and n<=59:
    print("D grade")
else:
    print("Fail")
