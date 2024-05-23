"""file to extract the names of the smORFs on the first row without repetitions on a tsv file generated from interpro-standalone"""

import csv

def gather_names_from_tsv(tsv_file):
    names = set()
    with open(tsv_file, 'r', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if row:  # To skip empty rows
                names.add(row[0])

    return names

def write_names_to_txt(names, output_file):
    with open(output_file, 'w') as file:
        for name in names:
            file.write(name + '\n')

# Example usage:
tsv_file = '/home/adriana/Downloads/rescored_microproteins_sars.fasta.tsv'
output_file = 'names_list.txt'

unique_names = gather_names_from_tsv(tsv_file)
write_names_to_txt(unique_names, output_file)
