import os
import sys

"""This script will be used to adhere the downloaded proteomes from ncbi-genome-download into
our own ORF files that were predicted using Predictorf in order to then use them as input
files for Orthofinder"""

def proteome_adherer(orf_folder, proteome_folder, outdir):
    files = os.listdir(proteome_folder)
    proteomes = {}
    for file in files:
        species_prot = file.replace(".faa", "")
        # print(species_prot)
        proteomes[species_prot] = f'{proteome_folder}/{file}'
        print(proteomes)

    orf_folders = os.listdir(orf_folder)
    for folder in orf_folders:
        files = os.listdir(f'{orf_folder}/{folder}')

        if not os.path.exists(f'{outdir}/{folder}'):
            os.mkdir(f'{outdir}/{folder}')

        for file in files:
            if not file.endswith("gORF"):
                if not file.endswith("tORF"):
                    filename = file.replace(".fasta", "")
                    # print(filename)
                    if filename.startswith("NZ") or filename.startswith("NC"):
                        filename = filename.split("_")
                        filename = filename[-2:]
                        filename = '_'.join(filename)
                        # print(filename)



                        if filename in proteomes:
                            cmd = f'cat {proteomes[filename]} {orf_folder}/{folder}/{file} > {outdir}/{folder}/{file}'
                            os.system(cmd)
                        else:
                            print(filename)




if __name__ == '__main__':
    # proteome_adherer(orf_folder='/home/adriana/tcc/smorfs/ortho_input_files/without_repeated_species',
    #                  proteome_folder='/home/adriana/tcc/smorfs/ortho_input_files/proteomes_renamed',
    #                  outdir='/home/adriana/tcc/smorfs/ortho_input_files/final_input_files')
    proteome_adherer(orf_folder=sys.argv[1], proteome_folder=sys.argv[2], outdir=sys.argv[3])

