# Find previously configured scaling srun scripts and run them.
# $1 is the directory name for scaling jobs.

scale=$1

for d in $(find $(pwd) -name $scale)
do
  n_scaled=$(ls $d/out/scale*.expt 2>/dev/null | wc -l )
  n_integrated=$(ls $d/../out/*_integrated.expt 2>/dev/null |wc -l)
  if [[ $n_scaled -eq 0 && $n_integrated -gt 0 ]]
  then
    chmod +x $d/srun.sh
    srun shifter $d/srun.sh
  fi
done
