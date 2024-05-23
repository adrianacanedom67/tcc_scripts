import sys
import os

from Bio import SeqIO


def fastaid_extractor(folder, outdir):
    files = os.listdir(folder)

    names = []

    for file in files:
        if file.endswith(".fasta"):
            records = SeqIO.parse(f'{folder}/{file}', 'fasta')
            for record in records:
                identifiers = str(record.description)
                # print(identifiers)
                full_names = identifiers.split(" ")
                # print(full_names)
                organisms = " ".join(full_names[0:2])
                # print(organisms)
                if f'>{organisms}\n' not in names:
                    names.append(f'>{organisms}\n')


    # print(names)

    with open(f'{outdir}/{file}.fasta', 'w') as outfile:
        outfile.writelines(names)


if __name__ == '__main__':
    fastaid_extractor(folder=sys.argv[1], outdir=sys.argv[2])
    # fastaid_extractor(folder='test', outdir='test')