#!/usr/bin/env python3

# Name: Odajiri Chinyere
# Matrikel Number: 811464
from ast import Not
import sys, os, re
import gzip


def PubDoi(filename,entry):
    goContents = []
    # just optional check for gzipness
    file = open(filename,'r')
    flag = False
    # a list would be as well a good idea
    res=""
    for line in file:
        if re.match("^ID",line):
            flag=False
            lineContent = line.split(" ")[3]
           # print(lineContent)
        if(re.match("^//",line)):
            if(len(goContents) == 0):
                res+=(lineContent+"\t"+"NA\n"+"\t"+"NA\n")
            else:
                for x in goContents:
                    res+=(lineContent+"\t"+x+"\n")
            goContents = []
            #EMPTY LIST
        else:
            if re.match("^RX\s\s\s",line):
                line=re.sub(".+PubMed=([0-9]+); DOI=([^;]+);","\\1\t\\2",line)
                goContents.append(line);          
    file.close()
    return res





def usage():
    print("""
Usage: OdasChi-test-2A.py --help|--filename UNIPROT-FILE ?--pumed PUMBED|--doi DOI-ID   
Uniprot-Parser by Odajri Chinyere , 2022
Extract information from Uniprot data files.
-------------------------------------------
Mandatory arguments are:
    ---filename -one compressed or uncompressed UNiprot
Optional arguments are:
    --help  - display this help page
    --pumbed -one Pumed id like 11157783
    --doi -one of pumbeed or --doi must be given
    """)
def main(argv):
    fileName = argv[0]
    if not os.path.isfile(argv[1]):
        print("Error: File '{}' does not exist!".format(argv[1]))
        return False

    if not re.match(".+\\.(dat|dat.gz)$",argv[1]):
        print("Error: File {} is not an Uniprot file! Uniprot files end in .dat or dat.gz!".format(argv[0]))
        return    

    if not argv[0] in ['--help','--filename', '--doi','--pumbed']:
        print("Error: Wrong cmd '{}', valid ones are '--help','--seqspecies'".format(argv[0]))
        return False

    if not re.match("[0-9]{8}",argv[2]):
        print("Invalid PumbMed ID, should have only Numbers")
        return False

    print("all fine but no functionality yet")


    
######################################
    if fileName == "--filename":
        print(PubDoi(argv[1],argv[2]),end="")
    
if __name__ == "__main__":
    if len(sys.argv) < 4:
        usage()
    else:
        main(sys.argv[1:])