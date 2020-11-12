import os
import sys
import re
from subprocess import run
from glob import glob

def maneggia():
    with open('energie', 'r') as f:
        for i, l in enumerate(f):
            if i==12:
                break
            en, nome=l.split()
            sempl=re.search('(clust..)', nome).groups()[0]
            compl=str(i)+'_'+sempl
            os.mkdir(compl)
            pdb=glob('*'+sempl+'*.pdb')[0]
            os.symlink('../'+pdb,compl+'/dna.pdb')
            os.symlink('../tox.sd', compl+'/tox.sd')
            # run(['gmx', 'pdb2gmx', '-f', 'dna.pdb',
            #     '-ff', 'amber99sb', '-water', 'tip3p'], cwd=compl)

if __name__ == '__main__':
    maneggia()
