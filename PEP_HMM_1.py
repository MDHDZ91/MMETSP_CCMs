#!/usr/bin/python
#MMETSP_sample_import.py
#inputs: (1) taxonomic classification of interest, (2) mmetsp taxa file with path
#outputs: rips and writes peptide fasta files and count data for each taxa

#import libraries
import sys
from ftplib import FTP #import the ftp library
import re 
import os
import numpy as np

######Get arguments from command line########
t=sys.argv[1] #full or partial taxa name
need='mmetsp_taxonomy.txt' #mmetsp taxa file with path

####Build files for HMM##########
#you only need to run this once
os.system('./mafft_hmmbuild.sh')

###########RETRIEVE NAMES!!##########
mt=open('mmetsp_taxonomy.txt','r')
g=[] #make an empty list to store genus names
for line in mt:
    if re.search(t,line): #if taxa name in line
        g= g+line.split('\t')[7:8]#pull out the 8th field should be genus, keeping as list

g=set(g) #keep only unique genus names
print g
#close the taxonomy file
mt.close()

ftp= FTP('ftp.imicrobe.us') #set home ftp server
ftp.login() #log in
ftp.cwd('camera/combined_assemblies') #ch

files=ftp.nlst() #make a list of all files and directories in wd
delimiter=' '
all=delimiter.join(files)

names=[]

for genus in g:
    string= genus+"\S*.pep.fa.gz"
    taxafiles=re.findall(string, all)
    print "{} files matching genus=".format(len(taxafiles))+genus
    print taxafiles
    if len(taxafiles) > 0:
        for filex in taxafiles:
            command = "RETR "+filex
            outfile = filex
            #ftp.retrbinary(command, open(outfile, 'wb').write)
            names.append(outfile)
            
ftp.quit()

print 'Part 1'

###########RETRIEVE PEP.FA##########
os.system('python ./MMETSP_sample_import.py {} {}'.format(t,need))
        
###########RETREIVE COUNTS##########
names2=[i.split('.')[0] for i in names] #removes .pep.fa.gz from the names

ftp= FTP('ftp.imicrobe.us') #set ftp server
ftp.login() #log in
ftp.cwd('camera/combined_assemblies') #change directory

#location for files
t=os.getcwd()
for ID in names2:
    #change to taxa directory/readcounts
    ripdir= ID+"/readcounts"
    ftp.cwd(ripdir) #change directory
    savefile= ID+"_cds_counts.txt" #saves files with unique names
    ftp.retrbinary('RETR cds.dat', open(savefile, 'wb').write)
    ftp.cwd("~/camera/combined_assemblies") #change directory to restart loop in right place
    
ftp.quit() 

print 'Part 2'

#if t=='Dinophyceae':
    #names.remove('Durinskia-baltica-CSIRO_CS-38.pep.fa.gz')
    #names.remove('Oxyrrhis-marina-CCMP1795.pep.fa.gz')
    #names.remove('Alexandrium-fundyense-CCMP1719.pep.fa.gz')

print names    
print 'Part 2B'

#########RUN HMM #########
for i in names:
    os.system('./MAGIC_HMM.sh {}'.format(i))
    
print 'COMPLETE'