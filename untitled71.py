# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 14:12:41 2024

@author: Rajesh
"""

import calendar
year=int(input())
cal=calendar.TextCalendar
year_c=cal.formatyear(year,1)
print(year_c)