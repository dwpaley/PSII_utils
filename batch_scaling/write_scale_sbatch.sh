scale_root=$1

SCRIPT_HOME=$CFS/m3562/dwpaley/scripts

stdout=$PWD/$scale_root.out stderr=$PWD/$scale_root.err envsubst < $SCRIPT_HOME/sbatch_template.sh > ${scale_root}_sbatch.sh
for d in $(find $PWD -type d -name $scale_root |sort)
do
  chmod +x $d/srun.sh
  echo echo srun shifter $d/srun.sh >> ${scale_root}_sbatch.sh
  echo srun shifter $d/srun.sh >> ${scale_root}_sbatch.sh
done

echo 'echo -n "Finished job @ t="; date +%s' >> ${scale_root}_sbatch.sh
