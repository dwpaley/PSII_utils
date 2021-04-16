# Write params_1.phil and srun.sh files for scaling jobs.
# Example:
# $ for d in run_*; do source ~/write_scale_phil.sh $d 002_rg003 scale; done
d=$1
t=$2
scale=$3

mkdir $d/$t/$scale
phil=$d/$t/$scale/params_1.phil
echo "input.path=$(pwd)/$d/$t/out" > $phil
echo input.experiments_suffix=_integrated.expt >> $phil
echo input.reflections_suffix=_integrated.refl >> $phil
echo "output.output_dir=$(pwd)/$d/$t/$scale/out" >> $phil
cat ~/scale_tail.phil >> $phil

mkdir $(pwd)/$d/$t/$scale/out

srun=$d/$t/$scale/srun.sh
cat ~/srun_head.sh > $srun
echo "cctbx.xfel.merge $(pwd)/$phil" >> $srun
