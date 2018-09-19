# This script will plot Ionizatio rate dN/dt with Current
# Pressure P=5E-12 torr, Voltage V=350KV
# Detailed calculation can be found on Note 89

'''
Created on September 19, 2018
@author:  Jyoti Biswas
'''

from matplotlib import cm

from pylab import figure
import matplotlib.pyplot as plt
import numpy as np
import math

#Pz = np.logspace(np.log10(1E-13) , np.log10(1E-10) , num=10)

I=np.array([1E-6, 1E-5, 1E-4, 1E-3, 3E-3, 5E-3])    # current in [A]



dN_dt = I*4.58E6  #

#plt.plot(Pz, dN_dQ,marker='o', linestyle='--', color='b')
plt.plot(I, dN_dt,marker='o', linestyle='--', color='b')

#plt.legend(loc='upper right');

plt.xlabel('Current [A]')
plt.ylabel(r'Ionization rate $[dN/dt]$')  # use dN/dt if needed

plt.xscale('log')
plt.yscale('log')
plt.tick_params(top='on', right='on', which='both', direction="in")

plt.savefig('ionization_rate/ionization_rate_dN_dt_with_Current.png', dpi = 300)   # save the figure to file
plt.show()
