import sys
import os

from Bio import SeqIO


def merge_files(folder, outdir):
    files = os.listdir(folder)

    organisms_names = []

    for file in files:
        records = SeqIO.parse(f'{folder}/{file}', 'fasta')
        for record in records:
            identifiers = str(record.description)
            if identifiers not in organisms_names:
                organisms_names.append(identifiers)
                organisms_names.append("\n")

                # print(records)

    with open(f'{outdir}/{file}.fasta', 'w') as outfile:
        outfile.writelines(organisms_names)


if __name__ == '__main__':
    merge_files(folder=sys.argv[1], outdir=sys.argv[2])
    # merge_files(folder='test', outdir='test')