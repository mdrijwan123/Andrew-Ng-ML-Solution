# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 23:29:58 2019

@author: MD RIJWAN
"""
import numpy as np
from numpy import random as rand
import scipy.linalg as alg
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

#Ones
on=np.ones((5,5))
#Zeros
ze=np.zeros((5,5))
#Random
ran=rand.rand(2,3)
#Plot
w=-6+np.sqrt(10)*rand.randn(1000)
sb.set_style('darkgrid')
sb.distplot(w)
plt.hist(w)
plt.show()
#Size
A=np.array([[1,2],[3,4],[5,6]])
np.shape(A)

str="GeeksPython"

A=np.array([[1,2,3],[4,5,6],[7,8,9]])
g_x=1/(1+np.exp(-A.T))
A=np.c_[np.ones(3),A]
np.ones(3)
t=np.linspace(0,10,100)
y=-3+5*t
plt.plot(t,y,c='r')


list1=[]
list1.append(['Name1','Name2'])
list1.append(['Name3','Name4'])

for i in zip(list1):
    k,l=i
    print(k,'and',l)





























