import os
import sys

from Bio import SeqIO


def extract_smorfs(folder, outdir):
    """

    :param folder: folder containing fasta files to be filtered
    :param outdir: output directory that will contain the filtered fasta files
    """
    print("Filtering all fasta files in the provided folder.\n")

    if not os.path.exists(outdir):  
        os.mkdir(outdir)    

    files = os.listdir(folder) 
    for file in files:     
        records = SeqIO.parse(f'{folder}/{file}', 'fasta')  

        to_write = []  

        for record in records:  

            if len(str(record.seq)) <= 300:  # checks if the length of the sequence is 100 or shorter
                to_write.append(f'>{str(record.description)}\n{str(record.seq)}\n')  


        with open(f'{outdir}/{file}', 'w') as outfile:  

    print(f"All fasta files were filtered with success. Results written to {outdir}.")


if __name__ == '__main__':
    if sys.argv[1] == '-h':
        print('usage: smorf_extractor.py <folder> <outdir>\n'
              '<folder> is a directory containing multiple fasta files to be filtered.\n'
              '<outdir> is the output directory where the filtered fasta files will be written to.\n'
              'The current script only filters out sequences shorter than 101 amino acids (or nucleotides).\n'
              'You can change the script to make the user specify the length cutoff.')
    else:
        extract_smorfs(folder=sys.argv[1], outdir=sys.argv[2])

