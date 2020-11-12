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

def sfera(m):
    'calcola parametri sfera bb'
    atomi=list(m.get_atoms())
    o=np.zeros(3)
    for a in atomi:
        o=o+a.coord
    o=o/len(atomi)
    r=0.0
    for a in atomi:
        ra=la.norm(a.coord-o)
        r=max(r,ra)
    return o,r

def sfera_sfere(ge='**/*clust*/dna.pdb'):
    sfere=[sfera(leggi(nome)) for nome in glob(ge, recursive=True)]
    centri=[s[0] for s in sfere]
    raggi=[s[1] for s in sfere]
    centro=np.mean(centri, 0)
    raggio=np.max(raggi)+np.max(la.norm(centri-centro))
    return centro, raggio
