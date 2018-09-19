# This script will plot Ionizatio rate dN/dt with respect to Voltage V
# Pressure P is constant, Current I is constant
# Pressure P=5E-12 torr, Current = 1mA
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
from scipy.interpolate import spline
from scipy.interpolate import interp1d

# Following values can be obtained,
#  from cross_section_reiser.py and cross_section_area.py
V = np.array([100, 200, 350, 500, 600])
i_r = np.array([11.4, 6.810, 4.550, 3.615, 3.230])
i_rate = [i * 1000 for i in i_r]


f2 = interp1d(V, i_rate, kind='cubic')

xnew = np.linspace(100, 600, num=50, endpoint=True)

plt.plot(V, i_rate, 'o', xnew, f2(xnew), '--', c='b')

#plt.scatter(V,i_rate, s=20, c='b', marker="o")
#plt.plot(Vnew,i_rate_smooth)
plt.xlabel('Beam Energy [KeV]')
plt.ylabel(r'Ionization Rate $[dN/dt]$')

plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.tick_params(top='on', right='on', which='both', direction="in")

plt.savefig('ionization_rate/ionization_rate_dN_dt_with_Voltage.png', dpi = 300)
plt.show()
