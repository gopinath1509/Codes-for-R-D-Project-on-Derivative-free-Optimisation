import numpy as np
import utils as ut
from matplotlib import pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

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


def func1(x):
    val = 0

    return val

def ackley(x, a=20, b=0.2, c=2*np.pi):
    """
    x: vector of input values
    """
    d = len(x) # dimension of input vector x

    sum_sq_term = -a * np.exp(-b * np.sqrt(sum(x*x) / d))
    cos_term = -np.exp(sum(np.cos(c*x) / d))
    return a + np.exp(1) + sum_sq_term + cos_term




def ackley_function(x1, x2):
    # returns the point value of the given coordinate
    part_1 = -0.2 * math.sqrt(0.5 * (x1 * x1 + x2 * x2))
    part_2 = 0.5 * (math.cos(2 * math.pi * x1) + math.cos(2 * math.pi * x2))
    value = math.exp(1) + 20 - 20 * math.exp(part_1) - math.exp(part_2)
    # returning the value
    return value


def ackley_function_range(x_range_array):
    # returns an array of values for the given x range of values
    value = np.empty([len(x_range_array[0])])
    for i in range(len(x_range_array[0])):
        # returns the point value of the given coordinate
        part_1 = -0.2 * math.sqrt(
            0.5 * (x_range_array[0][i] * x_range_array[0][i] + x_range_array[1][i] * x_range_array[1][i]))
        part_2 = 0.5 * (math.cos(2 * math.pi * x_range_array[0][i]) + math.cos(2 * math.pi * x_range_array[1][i]))

        value_point = math.exp(1) + 20 - 20 * math.exp(part_1) - math.exp(part_2)
        value[i] = value_point
    # returning the value array
    return value


def plot_ackley_general():
    # this function will plot a general ackley function just to view it.
    limit = 1000  # number of points
    # common lower and upper limits for both x1 and x2 are used
    lower_limit = -5
    upper_limit = 5
    # generating x1 and x2 values
    x1_range = [np.random.uniform(lower_limit, upper_limit) for x in range(limit)]
    x2_range = [np.random.uniform(lower_limit, upper_limit) for x in range(limit)]
    # This would be the input for the Function
    x_range_array = [x1_range, x2_range]
    # generate the z range
    z_range = ackley_function_range(x_range_array)
    # plotting the function
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.scatter(x1_range, x2_range, z_range, label='Ackley Function')

    def plot_ackley(x1_range, x2_range):

        # This would be the input for the Function
        x_range_array = [x1_range, x2_range]
        # generate the z range
        z_range = ackley_function_range(x_range_array)
        # plotting the function
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.scatter(x1_range, x2_range, z_range, label='Ackley Function')


########################### TEST ###################################
x = [i for i in range(200)]
y = [nesterov_function([i]) for i in range(200)]
y = np.asarray(y)
ut.my_plotter(x,y,0,210,np.amin(y), np.amax(y),'nestorov','x','y','plot')