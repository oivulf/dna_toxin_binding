from Bio import PDB
from Bio.PDB.PDBIO import PDBIO
import numpy as np
import numpy.linalg as la
import os
import subprocess as sp
from glob import glob
from string import Template

def centro(s):
    atomi=list(s.get_atoms())
    o=np.zeros(3)
    for a in atomi:
        o=o+a.coord
    o=o/len(atomi)
    return o

def centroide(ss):
    o=np.zeros(3)
    for s in ss:
        o=o+s[0]
    return o/len(ss)

def raggio(ss):
    o=centroide(ss)
    r=0.0
    for s in ss:
        r=max(r, la.norm(o-s[0]))
    return r

def accorpa(ss):
    md=1000.0
    n=len(ss)
    im=0
    jm=0
    for i in range(n):
        oi=ss[i][0]
        for j in range(i+1,n):
            oj=ss[j][0]
            # print(oj)
            d=la.norm(oi - oj)
            if d<md:
                im=i
                jm=j
                md=d
    ac=ss[im][1]+ss[jm][1]
    c=centroide(ac)
    ris=[(c, ac)]
    for i in range(n):
        if (i != im) and (i != jm):
            ris=ris+[ss[i]]
    return ris

def sfere():
    parser=PDB.PDBParser()
    m=parser.get_structure('m', 'dna.pdb')
    rr=m.get_residues()
    ss=[]
    for r in rr:
        c=centro(r)
        ss=ss+[(c,[(c,r)])]
    while len(ss)>5:
        ss=accorpa(ss)
    return ss

with open('prm.templ', 'r') as f:
    PRMT=Template(f.read())

def genera_prm(ss, i):
    o=ss[i][0]
    r=raggio(ss[i][1])
    prm=PRMT.substitute(cx=o[0], cy=o[1], cz=o[2], raggio=r+3)
    tn='rx_{}.prm'.format(i)
    with open(tn, 'w') as f:
        print(prm, file=f)
    return tn

def processa(ss, i):
    tn=genera_prm(ss,i)
    p=sp.run(['rbcavity', '-r', tn, '-W'])
    p=sp.run(['rbdock', '-r', tn, '-i', 'tox.sd', '-p', 'dock.prm'])

def tutto(c):
    os.chdir(c)
    ss=sfere()
    for i in len(ss):
        processa(ss,i)

