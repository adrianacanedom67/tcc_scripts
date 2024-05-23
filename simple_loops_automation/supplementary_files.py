"""to correct files to submit as supplementary files"""

import os

from Bio import SeqIO

def homolog_corrector(homolog_folder, outdir):
    homolog_files = os.listdir(homolog_folder)
    for homolog_file in homolog_files:
        records = SeqIO.parse(f'{homolog_folder}/{homolog_file}', 'fasta')
        to_write = []
        for record in records:
            identifiers = str(record.description)
            sequences = str(record.seq)
            identifiers = identifiers.replace("/home/farminfo/ACanedo/new_smorfs", "")
            to_write.append(f'>{identifiers}\n{sequences}\n')

            with open(f'{outdir}/{homolog_file}', 'w') as outfile:
                outfile.writelines(to_write)



if __name__ == '__main__':
    homolog_corrector(homolog_folder='/home/adriana/tcc/smorfs/homologs',
                      outdir='/home/adriana/tcc/smorfs/supplementary')