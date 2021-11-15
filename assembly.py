import os
import sys
import argparse
import glob

def fiching(path) :
    assembly_path = list(glob.glob(path+"/SRR*"))
    # print(assembly_path, len(assembly_path))

    assembly_files = []
    for paths in assembly_path :

    #     if paths == glob.glob(path+"/SRR*/*_assemby.fasta") :
    #         assembly_files.append(paths)
    # print(assembly_files)

    # assembly_file.append(glob.glob(path+"/SRR*/*_assembly.fasta"))
    # print(assembly_file, len(assembly_file))


def find_assembly(file) :
    pass




def main() :
    path = "/home/sdv/m2bi/rgoulancourt/Projet_long/data_projet_long_marqueur/marqueur_ok/all"
    fiching(path)

if __name__ == "__main__" :
    main()  