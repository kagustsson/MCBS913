#!/usr/bin/python3

import os, re
from shutil import copy

fasta_dir = '../../../../mcbs913kd/mcbs913sh/downloaded_genomes/fastas/'
gff_dir ='/home/mcbs913kd/mcbs913sh/downloaded_genomes/gffs/'


all_files = os.listdir(gff_dir)


completes = open('final_analysis_stuff/complete_genomes_list.txt','r')

completes_list = []

for line in completes.readlines():
    if "N/A" in line or line == "\n":
        continue
    else:
        print (line)
        tmp = re.findall(r"(GCF.*)\.",line)
        print (tmp)
        complete = tmp[0]
    #tmp1,tmp2 = line.split("\t")
    #complete, tmp3 = tmp2.split('\t')
        completes_list.append(complete)

print (completes_list)

count = 0

for file in all_files:
    for label in completes_list:
        if label in file:
            copy(gff_dir + file,'complete_genome_gffs/'+ file)
        else:
            count += 1
print (count)

