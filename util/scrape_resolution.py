import sys
import glob
import json
"""
Scrape logs from cctbx.xfel.merge to find images with a resolution cutoff below
a given value. 

Arguments are the cctbx.xfel.merge output directory and the resolution cutoff.

Usage examples:
$ python ~/scrape_logs.py run_000451.JF07T32V01_master/002_rg003/scale 3.5
$ for d in $(find . -type d -name out -path *scale*); do if [[ $(ls $d/*.expt 2>/dev/null |wc -l) -gt 0 ]]; then echo $d >&2; python ~/scrape_logs.py $d/.. 3.5; fi; done > frame_res.txt
"""

RESULTS="/global/cscratch1/sd/dwpaley/swissfel/results"
SCALE_DIR = sys.argv[1]
D_MAX = float(sys.argv[2])

id_image = {}
#expt_names = glob.glob(SCALE_DIR + "/../out/*_integrated.expt")
expt_names = glob.glob('/global/cscratch1/sd/dwpaley/psi/reindex/run702/*_integrated.expt')
for expt_name in expt_names:
  expt_json = json.load(open(expt_name))
  for expt in expt_json['experiment']:
    ident = expt['identifier']
    i_imageset = expt['imageset']
    imageset = expt_json['imageset'][i_imageset]
    image_index = "{}:{}".format(
        imageset['images'][0], 
        imageset['single_file_indices']
        )
    id_image[ident] = image_index




resolution_ident = []
#log_names = glob.glob(SCALE_DIR + "/out/*rank*.log")
log_names = glob.glob(SCALE_DIR + "/*rank*.log")
for log in log_names:
  with open(log) as f:
    log_lines = f.readlines()
  for l in log_lines:
    if 'resolution cutoff' not in l:
      continue
    try:
      res = float(l.split('resolution cutoff ')[1].split(',')[0])
      ident = l.split('experiment identifier ')[1].strip()
      resolution_ident.append((res, ident))
    except: pass


resolution_ident.sort(key=lambda l:l[0])

for r_i in resolution_ident:
  res, ident = r_i
  if res > D_MAX: break
  print("{:.3f}\t {}".format(
      res,
      id_image[ident]
      ))
