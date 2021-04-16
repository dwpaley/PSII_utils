"""
Take a BSREAD file, pick a single spectrum (by index in the corresponding run
file), downsample it to 100 points, and write it to a new h5 file in the format
used by Derek's script make_specs.py
"""

import sys
import h5py
import numpy as np
import matplotlib.pyplot as plt

run_n = sys.argv[1]
pulse_n = int(sys.argv[2])
out_fname = sys.argv[3]

N_POINTS = 100

unassembled_file = '/global/cfs/cdirs/m3562/restore/PSII_6555/data/dark/run_000{}.JF07T32V01.h5'.format(run_n)
beam_file = '/global/cfs/cdirs/m3562/swissfel/raw/PSII_6555/run_000{}.BSREAD.h5'.format(run_n)

data_pulse_ids = h5py.File(unassembled_file)['data/pulse_id'][()]
beam_h5 = h5py.File(beam_file)
beam_pulse_ids = beam_h5['data/SARFE10-PSSS059:SPECTRUM_CENTER/pulse_id'][()]
beam_energies = beam_h5['data/SARFE10-PSSS059:SPECTRUM_CENTER/data'][()]
beam_spectra_x = beam_h5['data/SARFE10-PSSS059:SPECTRUM_X/data'][()]
beam_spectra_y = beam_h5['data/SARFE10-PSSS059:SPECTRUM_Y/data'][()]

pulse_id = data_pulse_ids[pulse_n]
where = np.where(beam_pulse_ids==pulse_id)[0][0]
x = beam_spectra_x[where]
y = beam_spectra_y[where].astype(float)
ycorr = y-np.percentile(y, 10)
calc_energy = sum(x*ycorr)/sum(ycorr)

#this is terrible and I apologize...
e_ds = x[:len(x)//N_POINTS * N_POINTS].reshape(N_POINTS,-1).mean(axis=1)
y_ds = ycorr[:len(x)//N_POINTS * N_POINTS].reshape(N_POINTS,-1).mean(axis=1)
from cxid9114.parameters import ENERGY_CONV
wav_ds = ENERGY_CONV / e_ds


comp_args = {"compression":"gzip", "compression_opts":9, "shuffle":True}
wav_ds = np.array([wav_ds]).astype(np.float32)
e_ds = np.array([e_ds]).astype(np.float32)
y_ds = np.array([y_ds]).astype(np.float32)
calc_energy = np.array([calc_energy]).astype(np.float32)

with h5py.File(out_fname, 'w') as f:
  f.create_dataset("wavelengths", data=wav_ds, **comp_args)
  f.create_dataset("energies", data=e_ds, **comp_args)
  f.create_dataset("fluxes", data=y_ds, **comp_args)
  f.create_dataset("wave_ebeams", data=calc_energy, **comp_args)

import IPython;IPython.embed()
