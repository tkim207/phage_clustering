# phage_clustering
This repository holds the directions on clustering viruses or other MGEs

## Getting Started

These instructions will get let you calculate PI, PDI, and IDI based on a set of genomes.

### Prerequisites

python2
BLASTn
mcl

### Installing

You will need to download two scripts in this directory. No real installation required. But you can set path variables.

### Tutorial

First you have to do an all by all blast between your viruses.

`blastn -query newphage_LES_missing.fasta -subject newphage_LES_missing.fasta -evalue .01 -outfmt '6 std slen qlen' > blastfile` 

Then you have to run the Blast_to_MCL.1.py script in order to add up all the shared genomic regions between any two viruses

`Blast_to_MCL.1.py blastfile > blastfile.abc`

You need to run the awk command to filter any proportion of shared genomic region below 0.2 You can change this value to your liking.
  
`awk '{ if ($3 >= .2) print }' blastfile.abc > blastfile.filt.abc` 

Then simplify the file by using cut and so that you can put it into mcl.

`cut -f 1,2,3 blastfile.filt.abc > blastfile.filt.cut.abc`

These are the following mcl commands required. Your final cluster file will be in the dump file. Each row is a cluster.

`mcxload -abc blastfile.filt.cut.abc --stream-mirror -write-tab data.tab -o data.mci`

`mcl data.mci -I 2`

`mcxdump -icl out.data.mci.I20 -tabr data.tab -o dump.data.m20.I20`

Finally, you will build a new table you can feed into cytoscape so you can organize your clusters.

`mcl2tbl.py dump.data.m20.I20 > clustertbl.txt`
