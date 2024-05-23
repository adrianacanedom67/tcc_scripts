"""script to gather the missing sequences after the interpro scan, generating a list with the ones obtained and filtering
out the missing ones to finally create a new fasta file and run it on interpro"""

def read_fasta(fasta_file):
    sequences = {}
    current_sequence = None
    with open(fasta_file, 'r') as file:
        for line in file:
            if line.startswith('>'):
                current_sequence = line.strip()[1:]
                sequences[current_sequence] = ''
            else:
                sequences[current_sequence] += line.strip()
    return sequences

def write_fasta(sequences, output_file):
    with open(output_file, 'w') as file:
        for name, sequence in sequences.items():
            file.write('>' + name + '\n')
            file.write(sequence + '\n')

def generate_missing_fasta(original_fasta, names_list_file, output_fasta):
    names_set = set()
    with open(names_list_file, 'r') as file:
        for line in file:
            names_set.add(line.strip())

    original_sequences = read_fasta(original_fasta)
    missing_sequences = {name: sequence for name, sequence in original_sequences.items() if name not in names_set}

    write_fasta(missing_sequences, output_fasta)

# Example usage:
original_fasta = '/home/adriana/Downloads/rescored_microproteins_sars.fasta'
names_list_file = 'names_list.txt'
output_fasta = 'missing_sequences.fasta'

generate_missing_fasta(original_fasta, names_list_file, output_fasta)
