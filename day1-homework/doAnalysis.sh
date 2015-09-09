#!/bin/bash

echo "This Bash script should echo the commands to run FastQC and HISAT on all 24 samples.  e.g."
echo ""
echo "fastqc /Users/cmdb/qbb2015/rawdata/SRR072893.fastq.gz -o /Users/cmdb/qbb2015/assignments/day1-homework"
echo "hisat -p 4 -x /Users/cmdb/qbb2015/genomes/BDGP6 -U /Users/cmdb/qbb2015/rawdata/SRR072893.fastq.gz -S SRR072893.sam"
echo ""
echo "However, there are 6 mistakes!"

FASTQ_DIR=/Users/cmdb/qbb2015/rawdata
OUTPUT_DIR=/Users/cmdb/qbb2015/assignments/day1-homework

GENOME_DIR=/Users/cmdb/qbb2015/genomes/BDGP6
ANNOTATION=BDGP6.Ensembl.81.gtf

CORES=4

for i in:
  echo fastqc  -o /Users/cmdb/qbb2015/rawdata/SRR072893.fastq.gz /Users/cmdb/qbb2015/assignments/day1-homework
  echo hisat