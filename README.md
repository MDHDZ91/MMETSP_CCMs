# MMETSP_CCMs

CO2:
Format: CSV
CAMPEP,LogFC,logCPM
Keep a header, the script will ignore the first line and assign new headers

BLAST
Query- the last part of the identifier must be “|unique_name”
blastp -db _.pep.fa  -query _genesofinterest.txt  -out {species_name}_genetype_blast.csv  -outfmt “6 evalue qseqid ppos sseqid”
Columns will not have name but they are: Evalue,query sequence ID, percent match, sequence id
The script will give the file column names
HMM
Create seed files

>MAFFT Version 7
takes in seed file and gives alignment file
navigate to where you want the aligned file to rest
mafft gene_seed.txt>gene_seed_aln.txt
 
>HMM build from MAFFT
takes in aligned file from above and makes hmm file
navigate to gene_type folder
 @CF goes to .exe file output input
../hmmbuild OMT.hmm gene_seed_aln.txt
 
>HMM Search
takes hmm file from above
navigate to gene_type folder
@CF for GOC goes to .exe   file out 1 	file out 2  	input hmm  input pep.fa
../hmmsearch -o OMT_hmmout.csv --tblout test.csv  OMT.hmm ../PEPfa/Goc.pep.fa 

#####without CO2 from MMETSP website

Part I: PEP_HMM1.py
This is a bash file. 
Input: the name of species (group of organisms) from MMETSP
Output: HMM profiles for CCM and Photorespiration genes, counts from MMETSP

Part II: PEP_HMM2.ipynb
This script must be run on some python interface. Cannot run on shell because a function from pandas is not compatible with bash.

Make sure this script is in the same folder as the output from part I.

Input: the name of species (group of organisms) from MMETSP (same as in part I)
Output: Table with genes that map to CCMs and photorespiration for all the species in the group you selected.
