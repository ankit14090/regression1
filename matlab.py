# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 11:47:48 2018

@author: Ankit
"""
import matplotlib.pyplot as plt
x1=[123,25,88,255,258,144,9]
y1=[147,0,25,36,1.25,258,0]

x2=[147,0,25,36,1.25,258,0]
y2=[123,25,88,255,258,144,9]

x3=[17,2,250,36,25,258,100]
y3=[13,25,88,55,28,44,29]

plt.plot(x3,y3)
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.xlabel("Plot Number")
plt.ylabel("important var")

plt.title('how  funny')
plt.show()