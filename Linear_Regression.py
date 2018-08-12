# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 14:44:31 2018

@author: PRADEEP PANT
"""
from numpy import * 
import matplotlib.pyplot as pt


def error_computation(c,m,x1,y1):
    error=0
    cost=[]
    for i in range(0,len(x1)):
        x=x1[i]
        y=y1[i]
        error=(y-(m*x + c)) **2
        cost.append(error/float(len(x1)))
    return cost

def gradient_steps(c,m,x1,y1,learning_rate):
    c_grad=0
    m_grad=0
    for i in range(0,len(x1)):
        x=x1[i]
        y=y1[i]
        c_grad+=-(2/float(len(x1)))*(y-(m*x+c))
        m_grad+=-(2/float(len(x1)))*x*(y-(m*x+c))
    update_c = c - (learning_rate*c_grad)
    update_m = m - (learning_rate*m_grad)
    return [update_c,update_m]
    
def gradient_descent(x1,y1,initial_m,initial_c,learning_rate,itteration):
    m=initial_m
    c=initial_c
    for i in range(0,itteration):
        c,m=gradient_steps(c,m,x1,y1,learning_rate)
    return [c,m]


if __name__=='__main__':
    x1,y1=[],[]
    a= open('ex1data1.txt').readlines()
    for i in a:
        p=i.split(',')
        t = float(p[0])
        t=t**2
        x1.append(float(p[0]))
        y1.append(float(p[1]))
    #equation of line is y = mx + c
    point1_x = max(x1)
    point2_x = min(x1)
    learning_rate=0.0001
    initial_m=0
    initial_c=0
    itteration=1000
    [c,m]=gradient_descent(x1,y1,initial_m,initial_c,learning_rate,itteration)
    cost=error_computation(c,m,x1,y1)
    point1_y = m * point1_x + c
    point2_y = m * point2_x + c
    print "intercept value: ",c
    print "slopevalue: ",m
    pt.scatter(x1,y1)
    pt.plot([point1_x,point2_x],[point1_y,point2_y],c='r')
    pt.show()
    