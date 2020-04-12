# ASSIGNMENT 4
import numpy as np
import pylab
from scipy.special import gamma

# utility to interpolate P4(x) and Q4(x)
# from the given date sets a and b, respectively n and Gamma(n)
def interpolate(a,b):
    global first,  second, third, last, final
    first = []
    # computing first list of the newton divided differeces coeficients
    for i in range(4):
        if i+1 > len(a) : break
        # using the formula : D1(i) = (G(i+1)-G(i)) / (x(i+1)-x(i))
        new = (b[i+1]-b[i]) / (a[i+1]-a[i])
        first.append(new)
    second = []
    # computing the second list of the newton divided differeces coeficients
    for i in range(3):
        if i+1 > len(first) : break
        # using the same formula , but insted of x(i) , we use already computed
        # first coeficients, stored in the list first
        new = (first[i+1]-first[i]) / (a[i+2]-a[i])
        second.append(new)
    third = []
    # same logic follows here
    for i in range(2):
        if i+1 > len(second) : break
        new = (second[i+1]-second[i]) / (a[i+3]-a[i])
        third.append(new)
    last = []
    e = (third[1]-third[0]) / (a[4]-a[0])
    last.append(e)
    final = []
    # creating a list which will store all the previous coeficients and values for x and G(x)
    # in order to work only with one list
    final.append(a)
    final.append(b)
    final.append(first)
    final.append(second)
    final.append(third)
    final.append(last)
    # displaying the list for checking the obtained results
    for i in range(len(final)):
        print(final[i])
    return final

# costructing the polynomial from the previously computed coeficients
# for P4(x) and Q4(x)
def f(x,final):
    return final[1][0] + (final[2][0]*(x-final[0][0])) + (final[3][0]*(x-final[0][0])*(x-final[0][1])) + (final[4][0]*(x-final[0][0])*(x-final[0][1])*(x-final[0][2])) + (final[5][0]*(x-final[0][0])*(x-final[0][1])*(x-final[0][2])*(x-final[0][3]))
# the q(x) function
# q(x) = e^Q4(x)
def q(x,res):
    return np.exp(f(x,res))

# ploting the gamma function on [1,5]
x = pylab.linspace(1, 5, 1000) # 1000 linearly spaced numbers
pylab.plot(x, gamma(x), ls='-', c='k', label='$\Gamma(x)$')

# ploting the P4(x) with the given date set
a = [1,2,3,4,5]
b = [1,1,2,6,24]
P4 = interpolate(a,b)
y = f(x,P4)
pylab.plot(x,y)

# ploting the q(x) with the given date set
a1 = [1,2,3,4,5]
b1 = [0,0,np.log(2),np.log(6), np.log(24)]
q1 = interpolate(a1,b1)
y1 = q(x,q1)
pylab.plot(x,y1)
pylab.legend(["Gamma", "P4(x)", "q(x)"])
pylab.show() # show the plot

# Definitely the most accurate approximation for the Gamma function is the
# function q(x)
# From the graph : max error between Gamma and P4(x) is about 0.888-0.643 = 0.245
# while the max error between Gamma and q(x) is 0.926-0.916 = 0.01
