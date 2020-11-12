#!/bin/bash
PATH=$HOME/tossine/SimRNA_v3:$PATH
mkdir -p $1/p2
mkdir -p $1/p3
cd $1/p2
# raggruppa per cluster
ln -s ../prod.trafl .
clustering prod.trafl 0.01 3.5 5.0 7.0 >& clust.log
#
ln -s ../anneal-000001.pdb iniziale.pdb
ln -s ../data .
for t in prod_thrs7.00A_*.trafl; do
  SimRNA_trafl2pdbs iniziale.pdb $t 1 AA
done

