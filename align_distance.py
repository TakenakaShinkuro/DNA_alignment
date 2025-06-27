# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:06:26 2020

@author: 81805
"""


import sys 
import subprocess
from Bio.Align.Applications import MuscleCommandline
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import AlignIO

args = sys.argv

input_path = 'C:/Users/81805/Desktop/research_MGEs/genome_genbank_protein/fasta/20200625_LAB_178/LAB_178_16s.fasta'
#out_path = 'C:/Users/81805/Desktop/research_MGEs/sequence_identity_16S/LAB_178_dist_matrix.tsv'
out_path   = 'C:/Users/81805/Desktop/LAB_178_dist_matrix.tsv'
#input_path = args[1]
#out_path = args[2]

muscle_cline = MuscleCommandline(input=input_path)
child = subprocess.Popen(str(muscle_cline),
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         universal_newlines=True,
                         shell=(sys.platform!="win32"))



align = AlignIO.read(child.stdout, "fasta")

calculator = DistanceCalculator('identity')
dm = calculator.get_distance(align)

with open(out_path,"w") as f:
    f.write(str(dm))
    
    