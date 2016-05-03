#!/usr/local/bin/python3
#
# geneExtractor.py:
# Extract all 16S sequences from specified directories
# containing either fasta or gff files.
#
# @Joseph Sevigny, Kristin Agustsson
# 04/29/16

import os
import sys
import gzip
import seqIOTools

# ----------- global variables -----------------------
FASTA_dir = '/home/mcbs913kd/mcbs913sh/downloaded_genomes/fastas/'
GFF_dir = '/home/mcbs913kd/mcbs913sh/downloaded_genomes/gffs/'
out_dir = ''

gene_id = ('DNA_gyrase_subunit_B', 'XXXXXXXXXX')
pos_check = ('CDS', 'cds')
pos_flag = 'off'
neg_check = ('XXXXXX')
neg_flag = 'off'

output = set()

usageMsg = '''
Usage: geneExtractor.py [fasta directory] [gff directory] [output directory]
    Extract all 16S sequences from specified directories
    containing either fasta or gff files.
'''


def usage():
    if len(sys.argv) > 1 and sys.argv[1] == "-h":
        print(usageMsg)
        exit(0)

# -----------------------------------------------------------------------
# --------------------------- main --------------------------------------
# check argument usage correctness
usage()

# check arguments
if len(sys.argv) > 1:
    if not os.path.exists(sys.argv[1]):
        print(sys.argv[1] + ' does not exist.')
        exit(0)
    if not os.path.exists(sys.argv[2]):
        print(sys.argv[2] + ' does not exist.')
        exit(0)
    if not os.path.exists('gene_extract_' + sys.argv[3]):
        os.mkdir('gene_extract_' + sys.argv[3])

    FASTA_dir = sys.argv[1]
    GFF_dir = sys.argv[2]
    os.chdir('gene_extract_' + sys.argv[3])

    # create fasta/gff dictionary
    fa_gff_dict = seqIOTools.match_fasta_gff(
        os.listdir(FASTA_dir), os.listdir(GFF_dir))

    # extract genes from fasta/gff dictionary
    for f, g in fa_gff_dict.items():
        sample = f[:15]
        gene_count = 0

        # gene file will either be gzipped or not
        if g.endswith('.gz'):
            gfile = gzip.open(GFF_dir + g, 'rt')
        else:
            gfile = open(GFF_dir + g, 'r')

        # update progress
        sys.stdout.write("\rCurrent file: %s" % f)
        sys.stdout.flush()

        # extract gene
        for line in gfile.readlines():
            if line[0] == '#':
                continue
            else:
                for gene in gene_id:
                    neg_flag = 'off'
                    pos_flag = 'off'
                    if gene in line:
                        header, program, gid, start, stop, tmp, direction, \
                            tmp2, product = line.split("\t")
                        output.add(gid)

                        current_gfile = out_dir + f[:13] + '_' + gene + \
                            '_' + gid + '.fasta'

                        for n in neg_check:
                            if n in gid:
                                neg_flag = 'on'
                            else:
                                continue

                        for p in pos_check:
                            if p in gid:
                                pos_flag = 'on'
                            else:
                                continue

                        if pos_flag == "on" and neg_flag == "off":
                            gene_count += 1
                            seqIOTools.extract_region(f, header,
                                                      int(start), int(stop),
                                                      current_gfile,
                                                      direction,
                                                      str(gene_count) + "_" +
                                                      gid + "_" + f + "_" +
                                                      str(int(start)) + "_" +
                                                      str(int(stop)) +
                                                      "_" + direction)
                        # print (header, gid, str(start), str(stop), direction)
print(output)
