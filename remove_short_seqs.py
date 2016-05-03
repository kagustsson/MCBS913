#!/usr/bin/python3

from Bio import SeqIO

input = "all_16s.fasta"

output = open("best_16S.fasta", 'w')

for seq_record in SeqIO.parse(input, "fasta"):
    my_seq = (str(seq_record.seq))
    header = (str(seq_record.id))
    if len(my_seq) > 1000:
        output.writelines("\n>" + header + "\n" + my_seq)