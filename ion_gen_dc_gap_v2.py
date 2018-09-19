# This script will plot Ionizatio rate dN/dt with Pressure P
# Current I= 1mA, Voltage V=350KV is constant
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

Pz = np.logspace(np.log10(1E-13) , np.log10(1E-10) , num=10)

#dN_dQ = Pz*9.0978E17  # use E14, if dN/dt is needed for 1mA
dN_dt = Pz*9.0978E14  # Assume 1mA current

#plt.plot(Pz, dN_dQ,marker='o', linestyle='--', color='b')
plt.plot(Pz, dN_dt,marker='o', linestyle='--', color='b')

#plt.legend(loc='upper right');

plt.xlabel('Pressure[Torr]')
plt.ylabel(r'Ionization rate $[dN/dt]$')  # use dN/dt if needed

plt.xscale('log')
plt.yscale('log')
plt.tick_params(top='on', right='on', which='both', direction="in")

plt.savefig('ionization_rate/ionization_rate_dN_dt_with_Pressure.png', dpi = 300)   # save the figure to file
plt.show()
