import numpy as np
import utils as ut


def quadratic(H, b, x):
    value = 0.5 * np.dot(x,np.dot(H,x)) + np.dot(b,x)
    return value

def nesterov_function(x):
    n = len(x)
    value = 0.5*x[0]*x[0] + 0.5*x[n-1]*x[n-1] - x[0]
    for i in range(n-1):
        value += 0.5*(x[i+1] - x[i])*(x[i+1] - x[i])
    return value*0.25

def noise(x, xi, a, Delta):
    return xi*np.dot(x,a) + Delta*np.sin(np.linalg.norm(x))



########################### TEST ###################################
x = [i for i in range(200)]
y = [nesterov_function([i]) for i in range(200)]
y = np.asarray(y)
ut.my_plotter(x,y,0,210,np.amin(y), np.amax(y),'nestorov','x','y','plot')