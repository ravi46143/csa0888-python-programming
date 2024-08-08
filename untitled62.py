# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 09:41:15 2024

@author: Rajesh
"""

import queue
stack=queue.LifoQueue(4)
stack.put(10)
stack.put(20)
stack.put(100, timeout=1)
print(stack)