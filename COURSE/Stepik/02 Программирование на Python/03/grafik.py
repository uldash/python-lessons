# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 19:54:36 2018

@author: user
"""

from pylab import *

x = linspace(0, 5, 10)
y = x**2

figure()
plot(x, y, 'r')
xlabel('x')
xlabel('y')
title('title')
show()
