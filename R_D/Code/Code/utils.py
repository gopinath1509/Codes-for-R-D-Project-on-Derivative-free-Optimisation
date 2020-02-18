import os
import matplotlib.pyplot as plt
import numpy as np


def my_plotter(x,y,use = 0,xmin=0,xmax=0,ymin=0,ymax=0,label='na',xlabel='na',ylabel='na',title='na'):

    plt.figure()
    #plt.title('{} Accuracy for {} on MNIST'.format(curve_type.capitalize(), "MLP"))
    #plt.xlabel('Epoch')
    #plt.ylabel('{} Accuracy %'.format(curve_type.capitalize()))

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if (use == 1): # NAT VALUES || 0 ->  default values usually the best

        xmin = min(x)
        xmax = max(x)
        ymin = min(y)
        ymax = max(y)
        plt.ylim(ymin, ymax)
        plt.xlim(xmin, xmax)

    if (use == 2): # GIVEN VALUES

        plt.ylim(ymin, ymax)
        plt.xlim(xmin, xmax)

    plt.plot(x, y, label=label)
    plt.grid(ls='--')
    plt.legend()
    plt.show()
    return


