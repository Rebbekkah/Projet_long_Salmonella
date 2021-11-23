import os
import sys
import argparse


# def get_arguments() :
# 	parser = argparse.ArgumentParser(description = '')

# 	parser.add_argument('-i', '-input file', dest = 'gene_list', type = str, required = True, 
# 					help = "list of genes")

# 	parser.add_argument('-i', '-input file 1', dest = 'core_gene_list', type = str, required = True, 
# 	 				help = "list of complementary genes")

# 	 parser.add_argument('-k', '-input file 2', dest = 'accessory_gene_list', type = str, required = True, 
# 	 				help = "list of accessory genes")

# 	args = parser.parse_args()

# 	return args
	

def get_genes(file) :
	gene = ""
	with open(file, "r") as filin :
		for line in filin :	
			words = line.split()
			print(words[0][:-1])
	
	return words

	
				   
	




def main() :

	path_data = "/home/sdv/m2bi/rgoulancourt/Projet_long/data_projet_long_marqueur/marqueur_ok/all/roary_output_marqueur_ok/_1636985554_all/query_pangenome/pan_genome_results_intersection"
	#args = get_arguments()
	gene = get_genes(path_data)


if __name__ == "__main__" :
	main()


