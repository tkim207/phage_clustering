# phage_clustering

`blastn -query newphage_LES_missing.fasta -subject newphage_LES_missing.fasta -evalue .01 -outfmt '6 std slen qlen' > blastfile` 

`Blast_to_MCL.1.py blastfile > blastfile.abc`
  
`awk '{ if ($3 >= .2) print }' blastfile.abc > blastfile.filt.abc` 

`cut -f 1,2,3 blastfile.filt.abc > blastfile.filt.cut.abc`

`mcxload -abc blastfile.filt.cut.abc --stream-mirror -write-tab data.tab -o data.mci`

`mcl data.mci -I 2`

`mcxdump -icl out.data.mci.I20 -tabr data.tab -o dump.data.m20.I20`
