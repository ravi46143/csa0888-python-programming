# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:15:07 2024

@author: Rajesh
"""

dict={'a':5,'b':8,'c':6,'d':10}
sum=0
dict['c']=10
for i in dict.value():
    sum+=i
print(sum)
    