# ASSIGNMENT 1
import pylab
import numpy as np
import math
from numpy.linalg import norm

# utilities for ploting the function
x = np.linspace(0,5,100) # 100 linearly spaced numbers
y = np.exp(x - np.pi) + np.cos(x) - x + np.pi # our function

# compose plot
pylab.plot(x,y)
# the root will be 3.14
pylab.plot(3.14,0,'ro')
pylab.show() # show the plot

# function f(x)
def f(x):
    return np.exp(x - np.pi) + np.cos(x) - x + np.pi
# derivative of f(x)
def df(x):
    return np.exp(x-np.pi)- np.sin(x) - 1
# rewrited f(x) = 0  to  x = g(x)
# x = pi * e^(x-pi) + cos(x)
def g(x):
    return np.pi + np.exp(x - np.pi) + np.cos(x)

# function for newton method (as in previous assignment)
def newton1( x, err = 0.00001, iter = 100):
    print('\n\n*** NEWTON METHOD ***')
    for i in range(iter):
        newx = x - (f(x)/df(x))
        if abs(newx - x ) < err : break
        x = newx
        # displaying the results
        print('Iteration-%d, x = %0.5f and f(x) = %0.7f and df(x) = %0.5f and x(n+1) = %0.5f' % (i, x, f(x), df(x),newx))
    return newx, i

# utility for fixed point iteration
def fixedPointIteration(x0, e, N):
    print('\n\n*** FIXED POINT ITERATION ***')
    # number of iterations
    step = 1
    flag = 1
    # error condition
    condition = True
    while condition:
        # using the formula for fixed point iteration
        # x(n+1) = g(x(n))
        x1 = g(x0)
        print('Iteration-%d, x1 = %0.5f and f(x1) = %0.5f' % (step, x1, f(x1)))
        # updating the new value for x0
        x0 = x1
        # incrementing the numbers of iterations
        step = step + 1

        # setting a flag in case that the max number of iteration exited the
        # indicated bounds , if so break the loop and print "Not Convergent"
        if step > N:
            flag=0
            break
        # cheking if the condition is true of false
        # f(x1) > tolerance
        # if True then repeat again the while loop
        condition = abs(f(x1)) > e
    # after the root were found, print it
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    # in case the function does not converge
    else:
        print('\nNot Convergent.')


# x0 is the initial guess
x0 = 2
# e - tolerance
e = 0.00001
# N - max number of iterations ,
# NOTE : if N is less then 304 , then we will not be able to find the root
# with the required tolerance, for this specific case
N = 305
# calling the utility for fixed point iteration
fixedPointIteration(x0,e,N)

# Comparing the fixed point iteration results with the newthon method results
# we can see that the number of iteration in case of Newton method is much
# smaller than in fixedPointIteration algorithm , and as well we get a better
# precision in case of Newton method
x1, n1 = newton1(2)
print("The root is %f at %d iter" % (x1,n1))
