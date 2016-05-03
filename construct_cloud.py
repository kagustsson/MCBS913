#!/usr/bin/python3

import sys
import mycloud

str = ''

file = open(sys.argv[1], 'r')

for line in file:
    str += line.rstrip()# + ","
mycloud.generate_cloud(str,'word_out')