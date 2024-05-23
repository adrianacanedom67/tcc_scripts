"""to correct files that begin with a space after >"""
import os
from Bio import SeqIO

def fasta_formatter(file, outdir):
    records = SeqIO.parse(f'{file}', 'fasta')
    to_write = []
    for record in records:
        identifiers = str(record.description)
        # print(identifiers)
        # if identifiers.startswith(" "):
        identifiers = identifiers.replace(" ", "")
        print(identifiers)
        to_write.append(f'>{identifiers}\n')

    with open(f'{outdir}/file', 'w') as outfile:
        outfile.writelines(to_write)


if __name__ == '__main__':
    fasta_formatter(file='/home/adriana/tcc/smorfs/supplementary/orthologues/all_orthologues.fasta',
                    outdir='/home/adriana/tcc/smorfs/supplementary/orthologues/corrected')