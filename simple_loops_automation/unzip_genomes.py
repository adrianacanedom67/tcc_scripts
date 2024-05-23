import os
import sys


def unzip(folder):

    files = os.listdir(folder)
    for file in files:
        if file.endswith(".gz"):
            os.system(f'gunzip {folder}/{file}')

if __name__ == '__main__':
    # unzip(folder='/home/adriana/tcc/smorfs/ortho_input_files/ncbi-gen-down')
    unzip(folder=sys.argv[1])
