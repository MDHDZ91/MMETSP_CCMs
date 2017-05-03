#! /usr/bin/env bash
#

for i in SLC4 Bestrophin CA_beta CA_delta CA_alpha CA_zeta GOX GDCT PGP GCL HR SPT TSR ICL PK PEPC PEPCK MDH OMT ME PPDK PYC SHMT MS GlcDH ALAT_GGAT GK
	do 
		mafft "$i".txt> "$i"_aln.txt
		./hmmbuild "$i".hmm "$i"_aln.txt
	done