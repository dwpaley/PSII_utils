Tools for running batched indexing, scaling, and merging jobs at NERSC.

The main problem is that our standard workflow is to submit ~2 jobs (index and
scale) per run, while the slurm queueing system effectively penalizes people who
submit many small jobs because they all go through the queue sequentially. For
quick turnaround of many small jobs, it's more efficient to queue one big batch
that can spawn or srun many individual tasks.

Example scripts for indexing by this strategy are in a separate repo:
git@github.com:dwpaley/mdg_scripts. Example scripts for scaling are in this
repo. A few contemporaneous notes follow:

```
To run a bunch of scaling jobs on existing integration results:

in results directory:
$ for d in run_*; do source ~/write_scale_phil.sh $d 002_rg003 test_scale; done
$ source $CFS/m3562/dwpaley/scripts/write_scale_sbatch.sh test_scale
$ sbatch test_scale_sbatch.sh
```
