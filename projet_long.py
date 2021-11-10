import os, sys
import argparse



def get_arguments() :
    parser = argparse.ArgumentParser(description = '')

    parser.add_argument('-1', 'sequence_1', dest = 'bovine', type = str, required = True, 
                    help = "bovine sequence from scaffolding with Medusa")

    parser.add_argument('-2', 'sequence_2', dest = 'poultry', type = str, required = True, 
                    help = "poultry sequence from scaffolding with Medusa")

    parser.add_argument('-ref', dest = 'reference', type = str, required = True,
                    help = 'reference file FASTA format')



#récupérer les mutations du fichier.g.vcf?

def get_mutation() :



def main() :
    #path_data = 
    args = get_arguments()



if __name__ == "__main__" :
    main()