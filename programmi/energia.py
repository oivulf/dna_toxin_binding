#!/usr/bin/python3
import os
import sys

def leggi(nt):
    en=1e6
    with open(nt, 'r') as f:
        for l in f:
            if len(l)<100:
                en=min(en, float(l.split()[-2]))
    print(en, nt)

if __name__ == '__main__':
    # nt=sys.argv[-1]
    for nt in sys.argv[1:]:
        leggi(nt)
