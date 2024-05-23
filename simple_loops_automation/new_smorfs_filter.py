import os
import sys

from Bio import SeqIO

def new_uprotein_extractor(folder, outdir):

    files = os.listdir(folder)
    single_hits = {}

    for file in files:
        records = SeqIO.parse(f'{folder}/{file}', 'fasta')
        for record in records:
            identifiers = record.description
            # print(identifiers)
            sequence = record.seq
            # print(sequence)
            if f'>{identifiers}' not in single_hits:
                single_hits[identifiers] = []
                single_hits[identifiers].append(f'>{identifiers}\n{sequence}\n')
            else:
                if len(record.seq) < single_hits[sequence]:
                    break
            print(single_hits)





if __name__ == '__main__':
    new_uprotein_extractor(folder='/home/adriana/tcc/smorfs/blastp/foldertest', outdir='/home/adriana/tcc/smorfs/blastp/test')
