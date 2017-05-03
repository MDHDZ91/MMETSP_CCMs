#! /usr/bin/env bash
#

for i in SLC4 Bestrophin CA_beta CA_delta CA_zeta CA_alpha GOX GDCT PGP GCL HR SPT TSR ICL PK PEPC PEPCK MDH OMT ME PPDK PYC SHMT MS GlcDH ALAT_GGAT GK
	do 
		#mafft "$i".txt> "$i"_aln.txt
		#./hmmbuild "$i".hmm "$i"_aln.txt
		./hmmsearch -o "$1"_"$i"_hmmout.csv --tblout "$1"_"$i"_HMM.csv "$i".hmm "$1"
	done 
	