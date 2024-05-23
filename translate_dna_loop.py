import os
import sys

from Bio.Seq import Seq
from Bio import SeqIO


def translate_smorfs(folder, outdir):

    if not os.path.exists(outdir):  # checks if the provided outdir exists
        os.mkdir(outdir)    # if not, creates the outdir folder


    files = os.listdir(folder)
    for file in files:
        records = SeqIO.parse(f'{folder}/{file}', 'fasta')

        to_write = []

        for record in records:
            coding_dna = record.seq.translate()
            print(coding_dna)
            to_write.append(f'>{str(record.description)}\n{coding_dna}\n')


        with open(f'{outdir}/{file}', 'w') as outfile:
            outfile.writelines(to_write)


    print(f"All coding sequences were translated with success. Results written to {outdir}.")


if __name__ == '__main__':
    if sys.argv[1] == '-h' :
        print('usage: coding_dna_translator.py <folder> <outdir>\n'
              '<folder> is the directory containing the fasta files in DNA format\n'
              '<outdir> is the output directory in which the new protein sequences will be stored\n')
    else:
        translate_smorfs(folder=sys.argv[1], outdir=sys.argv[2])


            