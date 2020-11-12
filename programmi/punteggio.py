#!/usr/bin/python3
from Bio import PDB
from Bio.PDB.PDBIO import PDBIO
import numpy as np
import numpy.linalg as la
import os
from glob import glob
import re

def score(fn):
    with open(fn) as f:
        ll=f.readlines()
    ris=[]
    for i,l in enumerate(ll):
        if l[:-1]=='>  <SCORE>':
            ris.append(float(ll[i+1]))
    return ris

def voto():
    sm=1000.0
    sim=0
    for fn in glob('addotto_*.sd'):
        s=score(fn)
        im=np.argmin(s)
        if s[im]<sm:
            sm=s[im]
            corr=fn
            sim=im
        print(s)
    print('minimo: ', sm, corr, sim)

if __name__=='__main__':
    voto()

