from Bio import PDB
from Bio.PDB.PDBIO import PDBIO
import numpy as np
import numpy.linalg as la
import os
from glob import glob

def leggi(nome):
    parser=PDB.PDBParser()
    m=parser.get_structure('m', nome)
    return m

def leggi_ref():
    parser=PDB.PDBParser()
    m=parser.get_structure('dt', 'dt.pdb')
    nomi=['N1', 'N3', 'C5', 'C7', 'O3\'', 'P']
    ad={}
    for a in m.get_atoms():
        if a.name in nomi:
            ad[a.name]=a
    return ad

ref=leggi_ref()

def trova_atomo(r, nome):
    for a in r.get_atoms():
        if a.name==nome:
            return a
    return None

def aggiusta(r):
    if r.resname=='  U':
        r.resname=' DT'
        c5=trova_atomo(r, 'C5')
        n1=trova_atomo(r, 'N1')
        n3=trova_atomo(r, 'N3')
        p13=(n1.coord+n3.coord)/2
        p7d=c5.coord-p13
        p7d=p7d/la.norm(p7d)
        p7d=c5.coord+p7d*1.5
        c7=ref['C7'].copy()
        c7.coord=p7d
        r.add(c7)
    elif r.resname=='  A':
        r.resname=' DA'
    elif r.resname=='  G':
        r.resname=' DG'
    elif r.resname=='  C':
        r.resname=' DC'
    else:
        raise 'residuo inatteso'
    if r.id[1]==1:
        for a in ['P', 'OP1', 'OP2']:
            r.detach_child(a)
    r.detach_child('O2\'')
    return r

def aggiusta_pdb(nome, sav='../p3/'):
    m=leggi(nome)
    for r in m.get_residues():
        aggiusta(r)
    io=PDBIO()
    io.set_structure(m)
    io.save(sav+nome)

def aggiusta_glob(g):
    for f in glob(g):
        aggiusta_pdb(f)

