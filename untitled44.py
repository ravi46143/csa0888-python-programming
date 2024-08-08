# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 12:30:17 2024

@author: Rajesh
"""

list_a=[14,2,17,11,45,34,0,222]
list_b=[32,43,13,334,12,555,1,34]
list_a=sorted(list_a)
list_b=sorted(list_b)
list_a.extend(list_b)
print(sorted(list_a))