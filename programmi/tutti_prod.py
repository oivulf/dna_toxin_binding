import sys
import os
import subprocess as sp

tutte=["AF_1", "AF_AB3", "F10", "FB1_39", "FB1_39T3"]

def simrna_prod(dir):
    # os.chdir(dir)
    with open(dir+'/prod.log', 'w') as log:
        p=sp.Popen(["../SimRNA_v3/SimRNA", "-p", "anneal_minE.pdb", "-c", "../simrna_prod.conf",
                    "-o", "prod"], stdout=log, stderr=log, cwd=dir)
    return p


def fai():
    pi=[simrna_prod(d) for d in tutte]
    for p in pi:
        p.wait()

