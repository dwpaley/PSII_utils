"""
Check for shots where the given beam energy does not match the spectrum
"""
import sys
import h5py
import numpy as np
import matplotlib.pyplot as plt

run_n = sys.argv[1]

unassembled_file = '/global/cfs/cdirs/m3562/restore/PSII_6555/data/dark/run_000{}.JF07T32V01.h5'.format(run_n)
beam_file = '/global/cfs/cdirs/m3562/swissfel/raw/PSII_6555/run_000{}.BSREAD.h5'.format(run_n)

data_pulse_ids = h5py.File(unassembled_file)['data/pulse_id'][()]
beam_h5 = h5py.File(beam_file)
beam_pulse_ids = beam_h5['data/SARFE10-PSSS059:SPECTRUM_CENTER/pulse_id'][()]
beam_energies = beam_h5['data/SARFE10-PSSS059:SPECTRUM_CENTER/data'][()]
beam_spectra_x = beam_h5['data/SARFE10-PSSS059:SPECTRUM_X/data'][()]
beam_spectra_y = beam_h5['data/SARFE10-PSSS059:SPECTRUM_Y/data'][()]

reported_energies = []
calc_energies = []

n=0
import IPython;IPython.embed()
for i, pulse_id in enumerate(data_pulse_ids):
  where = np.where(beam_pulse_ids==pulse_id)[0][0]
  x = beam_spectra_x[where]
  y = beam_spectra_y[where].astype(float)
  ycorr = y-np.percentile(y, 10)
  calc_energy = sum(x*ycorr)/sum(ycorr)
  reported_energy = beam_energies[where]
  reported_energies.append(reported_energy)
  calc_energies.append(calc_energy)
  #if abs(reported_energy-calc_energy)>20: 
  if i<10:
    print(i)
    n+=1
    plt.plot(x,y)
    rep = reported_energy[0]
    calc = calc_energy
    plt.plot((rep, rep), (0, 20000), 'r-')
    plt.plot((calc, calc), (0, 20000), 'b-')
    plt.show()

plt.show()

#import IPython;IPython.embed()

plt.scatter(reported_energies, calc_energies)
plt.show()










