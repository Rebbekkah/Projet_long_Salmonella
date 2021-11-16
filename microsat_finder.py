import os
import sys
import argparse



def get_arguments() :
	parser = argparse.ArgumentParser(description = '')

	parser.add_argument('-i', '-input file', dest = 'sequence', type = str, required = True, 
					help = "fasta file where to find microsatellites")
	parser.add_argument('-l', '-length', dest = 'length', type = int, required = True, 
					help = "length of the repetition")
	parser.add_argument('-n', '-number', dest = 'number', type = int, required = True, 
					help = "number minimum of repetition of the tandem")
	args = parser.parse_args()

	return args
	
	
def read_fasta(sequence) :
	with open(sequence, "r") as filin :
		garde = ""
		seq1 = ""
		seq2 = ""
		for line in filin :
			if line.startswith('>') :
				if len(seq1) > len(garde) :
					garde = seq1
				seq2 = seq1
				seq1 = ""
			else :
				seq1 += line.strip()		

	with open(sequence+".txt", "w") as fasta_out :
		#print(sequence+".txt")
		for aa in garde :
			#print(aa)
			fasta_out.write(aa)

	return garde
	

def repetition(sequence) :
	#for aa in sequence :
	pass	


def main() :
	#path_data = 
	args = get_arguments()

	seq = read_fasta(args.sequence)
	tandem = repetition(seq)

if __name__ == "__main__" :
	main()


