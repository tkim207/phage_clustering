#!/usr/bin/python

import sys

with open(sys.argv[1]) as dumpfile:
   cluster=1
   order=1
   for line in dumpfile:
      for phage in line.strip().split('\t'):
         print phage+'\t'+str(cluster)+'\t'+str(order)
	 order=order+1
      cluster=cluster+1
