import os
import sys

from Bio import SeqIO

def file_rename(folder, outdir):
    files = os.listdir(folder)

    for file in files:
    # print(folder)
    # print(file)
        if file.endswith(".faa"):
            records = SeqIO.parse(f'{folder}/{file}', 'fasta')
            for record in records:
                entry = record.description
                if "MULTISPECIES" not in entry:
                    names = entry.split("[")
                    # print(names)
                    species_names = names[-1].split(" ")
                    # print(species_names)
                    species = '_'.join(species_names)
                    # print(species)
                    species = species.replace("[", "").replace("]", "")
                    print(species)
                    cmd = f'cp {folder}/{file} {outdir}/{species}.faa'
                    os.system(cmd)
                    # print(cmd)
                    break

if __name__ == '__main__':
    file_rename(folder=sys.argv[1], outdir=sys.argv[2])
    # file_rename(folder='/home/adriana/PycharmProjects/tcc/scripts/test', outdir='/home/adriana/PycharmProjects/tcc/scripts/outdir_test')