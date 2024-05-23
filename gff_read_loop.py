import os
import sys


# def loop_gffread("/home/adriana/tcc/smorfs/sequences/new_orfs/", "/home/adriana/tcc/smorfs/sequences/new_orfs/fasta_orfs/"):
def loop_gffread(folder, outdir):

    """
    folder: the path to the folder containing the genomes.fasta and the gff files. They MUST have the same name,
    except for the format (fasta or gff).
    outdir: the output directory where all files will be written to.
    """

    # this lists all the files in the provided 'folder'
    files = os.listdir(folder)

    # looping through the files
    for file in files:
        if file.endswith("fna"):  # checking where it is a fasta file
            gff = file.replace(".fna", ".fna.gff")   
            cmd = f'gffread {folder}/{gff} -g {folder}/{file} -w {outdir}/{file.replace(".fasta", ".fna")}'

            os.system(cmd)


if __name__ == '__main__':
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print("usage: loop_gffread.py <folder> <outdir>\n"
              "folder: the path to the folder containing the genomes.fasta and the gff files. They MUST have the same "
              "name, except for the format (fasta or gff). \n"
              "outdir: the output directory where all files will be written to.\n")
    else:
        loop_gffread(folder=sys.argv[1], outdir=sys.argv[2])
