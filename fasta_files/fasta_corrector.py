import os

from Bio import SeqIO

"""this script is to format those homolog files (add the '>' and remove extra'.fasta' from filename)"""

def fasta_corrector(folder, outdir):
    files = os.listdir(folder)

    for file in files:
        # records = SeqIO.parse(f'{folder}/{file}', 'fasta')
        # for record in records:
        outfile = file.replace(".fasta", "").replace(".fasta", "")

        # cmd = f" sed 's/^\([^acgt]\)/>\1/'  {folder}/{file} > {outdir}/{file}"
        cmd = f"awk '{ if ($0 ~ /_/) { printf ">f"; } print $0; }' {folder}/{file} > {outdir}/{outfile}"
        os.system(cmd)


if __name__ == '__main__':
    fasta_corrector(folder='/home/adriana/tcc/smorfs/orthofinder_first_results/homologs',
                    outdir='/home/adriana/tcc/smorfs/orthofinder_first_results/homologs/homologs_corrected')
