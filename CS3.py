# ASSIGNMENT 3
import numpy as np
import math
from numpy.linalg import norm
import pylab


# function f(x)=0
# cos(x) - 1 = 0
def f(x):
    return np.cos(x) - 1
# functionn x = g(x)
def g(x):
    return np.cos(x) - 1 + x
# utility for fixed point iteration algorithm
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
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
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

# utility for bisection method
# the argumests a and b are the bounds from the formula
# of the min term : c=(a+b)/2
def bisection(a,b):
    # cheking if the sign is changeing on the interval [a,b]
    print("*******BISECTION METHOD************")
    if (g(a) * g(b) >= 0):
        print("You have not assumed right a and b\n")
        return
    # initialize min term
    c = a
    # count - vatiable to count number of iterations
    count = 0
    # while the interval is less than the tolerance
    while ((b-a) >= 0.0001):
        # Find middle point
        c = (a+b)/2
        # Check if middle point is root
        if (g(c) == 0.0):
            break
        print("lower bound = %.6f , upper bound = %.6f, mid term = %0.6f" %(a,b,c))
        # repeat the step , setting the right values for upper
        # and lower bound respectively
        if (g(c)*g(a) < 0):
            b = c
        else:
            a = c
        count+=1
    print("The number of iterations using bisection method is %d" %(count))
    print("The value of root is : ","%.4f"%c)

# assign values for a and b in a way that the sign on interval [a;b]
# for the function g(x) is changeing
a = -2
b = 3
# call the bisection method
bisection(a, b)

# x0 is the initial guess
x0 = 0.1
# e - tolerance
e = 0.00001
# N - max number of iterations ,
# NOTE : if N is less then 426 , then we will not be able to find the root
# with the required tolerance, for this specific case
N = 426
# calling the utility for fixed point iteration
fixedPointIteration(x0,e,N)
# comparing the bisection results with fixed point method we can observe
# that bisection method converges at a much higher speed, especialy when
# the values for a and b are good enought,if the value for a is positive b,
# then we get the complexity of O(1), which is the fastest one possible,
# while when the fixed point method is showing a poor result with at lest
# 426 iterations

# utilities for ploting the function
x = np.linspace(-4,5,100) # 100 linearly spaced numbers
y = np.cos(x) - 1 + x # g(x)
pylab.plot(0,0,'ro')

# compose plot
pylab.plot(x,y)
pylab.show() # show the plot
