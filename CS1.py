# ASSIGNMENT 1
# library for natural log
import numpy as np

# deafault values from expresion
a0 = 1.129241
a1 = 2.341077
a2 = 8.775468

# this function will return the value of our first equation at specific x and specific t
def f(x,t):
    return a0*pow(10,-3) + (a1*pow(10,-4)*np.log(x)) + (a2*pow(10,-8)*np.log(x)**3) - (1/(t+273.15))

# this function will return the value of the derivative of the first equation
def df(x):
    return (2.341077/(10000*x)) + (  26.326404*np.log(x)*np.log(x)/(100000000*x))

# function for Newton's method
# it takes as arguments x - our initial guess , t - which it upper and lower bound for
# the values of temperature form the equation , err - tolerance , iter - max number of
# iteration
def newton1( x,t, err = 0.00001, iter = 100):
    # to find the root would be enought 10 iteration
    for i in range(iter):
        # formula for newtons method :
        # x(n+1) = x(n) - [ f(x) / F(x) ]
        newx = x - (f(x,t)/df(x))
        # exit from the for loop when delta x is less than tolerance
        if abs(newx - x ) < err : break
        # update the value for x
        x = newx
    # return the root, and number of iteration wich were performed
    return newx, i

# calling the newtons method function for first equation
x1, n1 = newton1( 1500, 18.99)
print("Eq-1 : the root is %f at %d iter" % (x1,n1))
# calling the newtons method function for second equation
x2, n2 = newton1( 1500, 19.01)
print("Eq-2 : the root is %f at %d iter" %(x2,n2))
# printing the range
print("The range is %f" %(x1-x2))
