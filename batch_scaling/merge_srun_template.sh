#!/bin/bash

#cctbx
source /img/activate.sh

#for experiment database
export SIT_DATA=/global/cscratch1/sd/blaschke/lv95/psdm/data

#for psana
export SIT_PSDM_DATA=/global/cscratch1/sd/psdatmgr/data/psdm

#needed to open h5 files from workflow nodes. -DWP
export HDF5_USE_FILE_LOCKING=FALSE

# run
