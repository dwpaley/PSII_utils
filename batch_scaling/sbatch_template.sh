#!/bin/bash -l
#SBATCH --qos=regular
#SBATCH --job-name=swissfel
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --tasks-per-node=32
#SBATCH --constraint=haswell
#SBATCH --image=docker:dwpaley/cctbx-xfel:fix18t4
#SBATCH --mail-type=NONE
#SBATCH -A m3562
#SBATCH -o $stdout
#SBATCH -e $stderr
# base directory

# submit jobs

echo -n "Starting job @ t="; date +%s

