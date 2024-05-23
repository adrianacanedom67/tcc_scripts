import os
import sys


def orthofinder_loop(folder):
    folders = os.listdir(folder)

    for sub_folder in folders:
        files = os.listdir(f'{folder}/{sub_folder}')
        # print(files)
        cmd = f'~/programs/orthofinder/OrthoFinder/./orthofinder -f {folder}/{sub_folder}'
        os.system(cmd)

if __name__ == '__main__':
    orthofinder_loop(folder='/home/adriana/tcc/smorfs/ortho_input_files/final_input_files')






