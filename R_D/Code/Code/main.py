import numpy as np
import utils as ut
from algorithms import *
#import function as f
from ackley import *






def main():
    # Number of points to be used in the simulation
    n = 3

    # Number of iterations to be performed
    T = 10000

    x = [ np.random.uniform(-32.7,32.7)  for i in range(n) ]
    y = [ackley_function(x[i],0) for i in range(len(x))]

    ut.my_plotter(x,y,0)

    #for i in range(T):
















if __name__ == '__main__':
    main()