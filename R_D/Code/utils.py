import os
import matplotlib.pyplot as plt
import numpy as np


def my_plotter(x,y,xmin,xmax,ymin,ymax,label,xlabel,ylabel,title):

    plt.figure()
    #plt.title('{} Accuracy for {} on MNIST'.format(curve_type.capitalize(), "MLP"))
    #plt.xlabel('Epoch')
    #plt.ylabel('{} Accuracy %'.format(curve_type.capitalize()))

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    #plt.ylim(ymin, ymax)
    plt.xlim(xmin, xmax)

    plt.plot(x, y, label=label)
    plt.grid(ls='--')
    plt.legend()
    plt.show()
    return


