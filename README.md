# dna_toxin_binding
generating DNA aptamer configuration and docking toxins for in silico binding evaluation

this project aims to provide in silico prediction of binding for toxin-aptamer couples.
it consists of the following phases:
1. mutate dna.seq to rna.seq
2. SimRNA: initialization and annealing
3. SimRNA long dynamics
4. clusterization of RNA structures
5. generation of pdb all atom files for RNA structures
6. mutation to DNA through programmi/muta.py
7. docking toxins to DNA through RxDock (attracca.py):
  1. cluster residues into spheres
  2. generate RxDock configuration for each sphere from a template
  3. run RxDock grid generation
  4. run RxDock docking pose search
  5. run a statistical characterization of all the poses

a list of files and their functions can be found in Manifest
