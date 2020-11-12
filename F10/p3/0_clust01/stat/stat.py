from multiprocessing import Pool
import subprocess as sp

def esegui(ii, i):
    tn='rx_{}.prm'.format(i)
    with open('addotto_{}_{}.log'.format(i,ii), 'w') as log_i:
        print('eseguo processo {}'.format(ii))
        sp.run([
            'rbdock', 
            '-r', tn, 
            '-i', 'tox.sd', 
            '-p', 'dock.prm', 
            '-o', 'addotto_{}_{}'.format(i,ii)], stdout=log_i)

def tutti(i=3):
    with Pool(processes=100) as p:
        for ii in range(100):
            p.apply_async(esegui, (ii,i))
    p.join()

