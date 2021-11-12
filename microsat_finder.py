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
		seq = ""


		for line in filin :
			if line.startswith('>') :
				if len(seq) < 200 :
					print(seq, len(seq))
					#break
					seq = ""
			elif not line.startswith('>') :
				seq += line.strip()
			
			
			# else :
			# 	break
			# if line.startswith('>') :
			# 	continue
			# elif not line.startswith('>') :
			# 	seq += line.strip()
			# if:
			# 	break
		#print(line)


	# 	lines = filin.readlines()
	# 	print(lines[0:100])

	# 	for line in lines :
	# 		if line.startswith('>') :
	# 			continue
	# 		else : 
	# 			seq += line

	# print(seq[0:100])

	print(seq[0:200], len(seq))


def main() :
	#path_data = 
	args = get_arguments()

	read = read_fasta(args.sequence)

if __name__ == "__main__" :
	main()


