"""
Plot the first spectrum in an h5 file
"""


import sys
import h5py
import numpy as np
import matplotlib.pyplot as plt

infile = sys.argv[1]
f = h5py.File(infile)
wav = f['wavelengths'][()]
e = f['energies'][()]
y = f['fluxes'][()]
energy = f['wave_ebeams'][()]

plt.plot(e[0], y[0])
plt.show()
