#!/usr/local/bin/python3
#
# uclustPipeline.py:
# Run UCLUST commands and format output.
#
# @Kristin Agustsson
# 05/01/16
import os
import sys

# Globals
fasta_file = sys.argv[1]
min_percent = sys.argv[2]

# Step 1: Sort FASTA file
sorted_fasta_file = "sorted_" + fasta_file
os.system("uclust --sort " + fasta_file + "--output " + sorted_fasta_file)

# Step 2: Run sorted FASTA files for 95-100% identity
fasta_file_id = fasta_file + "_id.uc"
for p in range(min_percent, 100):
	os.system("uclust --input " + sorted_fasta_file + "--uc " + fasta_file_id + " --id " + p)

# Step 3: Sort step 2 output
sorted_fasta_file_clusters = sorted_fasta_file + "_clusters.fasta"
os.system("uclust --sortuc " + fasta_file_id + " --input " + fasta_file + "--output " + sorted_fasta_file_clusters)

# Step 4: .UC to .FASTA


