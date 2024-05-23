import os
import sys

from Bio import SeqIO


def loop_read(folder, outdir):
    files = os.listdir(folder)

    for file in files:
        cmd = f'python3 /home/adriana/PycharmProjects/eduardo/predictorf/predictorf.py --genome {folder}/{file} --output {outdir}/{file.replace(".fna", ".fasta")}'
        #this can be modified for any other .py file

        os.system(cmd)

if __name__ == '__main__':
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print("usage: loop_to read eduardo's code\n")

    else:
        loop_read(folder=sys.argv[1], outdir=sys.argv[2])




