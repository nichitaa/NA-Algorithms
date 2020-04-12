# ASSIGNMENT 5
import numpy as np
import pylab
from gekko import GEKKO

# utility to interpolate P4(x) and Q4(x)
# from the given date sets a and b, respectively n and Gamma(n)
def interpolate(a,b):
    global first,  second, third, last, final
    first = []
    # computing first list of the newton divided differeces coeficients
    for i in range(5):
        if i+1 > len(a) : break
        # using the formula : D1(i) = (G(i+1)-G(i)) / (x(i+1)-x(i))
        new = (b[i+1]-b[i]) / (a[i+1]-a[i])
        first.append(new)
    second = []
    # computing the second list of the newton divided differeces coeficients
    for i in range(4):
        if i+1 > len(first) : break
        # using the same formula , but insted of x(i) , we use already computed
        # first coeficients, stored in the list first
        new = (first[i+1]-first[i]) / (a[i+2]-a[i])
        second.append(new)
    third = []
    # same logic follows here
    for i in range(3):
        if i+1 > len(second) : break
        new = (second[i+1]-second[i]) / (a[i+3]-a[i])
        third.append(new)
    forth = []
    for i in range(2):
        if i+1 > len(third) : break
        new = (third[i+1]-third[i]) / (a[i+4]-a[i])
        forth.append(new)
    e = (forth[1]-forth[0]) / (a[5]-a[0])
    last = []
    last.append(e)
    final = []
    # creating a list which will store all the previous coeficients
    # in order to work only with one list
    final.append(a)
    final.append(b)
    final.append(first)
    final.append(second)
    final.append(third)
    final.append(forth)
    final.append(last)
    # displaying the list for checking the obtained results
    for i in range(len(final)):
        print(final[i])
    return final

# constructing the polinomyal after the formula
# P5(x) = b1 + b2(x-x1) + b3(x-x1)(x-x2) + b4(x-x1)(x-x2)(x-x3) + b5(x-x1)(x-x2)(x-x3)(x-x4) + b6(x-x1)(x-x2)(x-x3)(x-x4)(x-x5)
# where b1,b2...b6 are the coeficients of the newton divided differeces method
def f(x, r):
    return r[1][0] + (r[2][0]*(x-r[0][0])) + (r[3][0]*(x-r[0][0])*(x-r[0][1])) + \
            (r[4][0]*(x-r[0][0])*(x-r[0][1])*(x-r[0][2])) + \
            (r[5][0]*(x-r[0][0])*(x-r[0][1])*(x-r[0][2])*(x-r[0][3])) +\
            (r[6][0]*(x-r[0][0])*(x-r[0][1])*(x-r[0][2])*(x-r[0][3])*(x-r[0][4])) \

# points to be interpolated
# list a contains the values for x axix
# list b contains the valurs for the y axix
a = [2,4.5,5.25,7.81,9.2,10.6]
b = [7.2,7.1,6,5,3.5,5]
# calling the interpolate function to get the necessary coeficients
u = interpolate(a,b)


# Ploting the final results on interval [1,12]
x = np.linspace(1,12,100) # 100 linearly spaced numbers
y = f(x, u) # getting the value for the function on the interval [1,12]
pylab.plot(x,y) # ploting the polynomial I obtained after using newton divided differeces method

# final step is to plote the cubic spline for the given data sets
# creating the object GEKKO , for using in build library fuction
# for cubic splines plot
m = GEKKO()
m.xm = m.Param(value=x) # setting the interval xm to be the same as interval x
m.ym = m.Var()  # calculating the y values
m.cspline(m.xm, m.ym, a, b) # computing the cubic spline for lists a and b
m.options.IMODE=2
m.solve(disp=False) # wihtout displaying 100 obtained points from the cspline fuction

pylab.plot(a,b,'bo', label="data") # ploting the points x and y
pylab.plot(m.xm, m.ym, 'r--', label='cubic spline') # ploting the results for cubic spline
pylab.legend(["P5(x)", "data", "cubic splines"]) # legend for the plot
pylab.show() # displaying the obtained graph
# we can definitely see how accurate the cubic splines interpolated the data
# comparatively to the polinomyal, the shortest path will be provided by the cubic splines
