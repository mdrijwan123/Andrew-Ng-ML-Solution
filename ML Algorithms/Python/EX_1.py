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
