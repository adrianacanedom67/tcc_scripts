import os

from Bio import SeqIO

"""since some softwares require to have one sequence per file, this script is for this"""

def seq_divider(file, outdir):
    records = SeqIO.parse(f'{file}', 'fasta')
    for record in records:
        identifier = record.description
        sequence = record.seq

        with open(f'{outdir}/{identifier}.fasta', 'w') as outfile:
            outfile.writelines(f'>{identifier}\n{sequence}\n')



if __name__ == '__main__':
    seq_divider(file='/home/adriana/tcc/smorfs/sequences/sequences_for_idps/smorfs_t1.fasta',
                outdir='/home/adriana/tcc/smorfs/sequences/sequences_for_idps/one_seq_per_file')