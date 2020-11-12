import sys
import os
import subprocess as sp

tutte=["AF_1", "AF_AB3", "F10", "FB1_39", "FB1_39T3"]

def simrna_anneal(dir):
    # os.chdir(dir)
    with open(dir+'/anneal.log', 'w') as log:
        p=sp.Popen(["../SimRNA_v3/SimRNA", "-s", "rna.seq", "-c", "../simrna_anneal.conf",
                    "-o", "anneal"], stdout=log, stderr=log, cwd=dir)
    return p


def fai():
    pi=[simrna_anneal(d) for d in tutte]
    for p in pi:
        p.wait()

