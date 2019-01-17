# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

data=np.array([[1,0],[3,1],[4,0],[2,0],[7,1],[8,0],[9,1],[5,1],[6,0],[10,0]])
data=np.c_[np.ones(10),data]
X=data[:,0:2]
y=X[:,1]
def LScostFunction(X,y,theta):
    m=len(y)
    h=(1/(1+np.exp(-X.dot(theta))))
    #J=(-1/m)*(((np.log(h).T.dot(y)))+((np.log(1-h).T.dot(1-y))))
    J=-1*(1/m)*(np.log(h).T.dot(y)+np.log(1-h).T.dot(1-y))
    if np.isnan(J[0]):
        return(np.inf)
    return(J[0])
temp=LScostFunction(X,y,[[-0.4],[0.06]])
J=[]
def GradientDescent(X,y,theta=np.array([[0],[0]]),alpha=0.1):
    m = y.size
    h=(1/(1+np.exp(-X.dot(theta.reshape(-1,1)))))
    grad =(1/m)*X.T.dot(h-y)
    return(grad.flatten())
    #sqerror=X.T.dot(h-y)
    #theta=theta-alpha*(1/m)np.sum(sqerror)
    #J_temp=LScostFunction(X,y,theta)
    

Theta=GradientDescent(X,y)
print(Theta)

