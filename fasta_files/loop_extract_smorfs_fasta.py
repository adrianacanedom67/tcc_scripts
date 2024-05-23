from Bio import SeqIO
import sys
import os

def loop_extractsmorfs(input_handle, output_handle):
    files = os.listdir(input_handle)

    for file in SeqIO.parse(files, "fasta"):
        if len(file.seq) <= 100 :
            files.append(file)

    SeqIO.write(files, output_handle, "fasta")

if __name__=="__main__" :
    loop_extractsmorfs(input_handle=sys.argv[1], output_handle=sys.argv[2])




