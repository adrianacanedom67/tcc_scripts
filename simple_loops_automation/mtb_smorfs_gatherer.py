import os


"""this script is for gathering the files of individual mtb_smorfs and put them in their corresponding directories"""

def smorf_gatherer(mtb_folder, outdir):
    mtb_folders = os.listdir(mtb_folder) #dont forget that inside these folder are the files I need
    for folder in mtb_folders:
        seq_files = os.listdir(f'{mtb_folder}/{folder}')

        if not os.path.exists(f'{outdir}/{folder}'):
            os.mkdir(f'{outdir}/{folder}')

        for file in seq_files:
            if file.startswith("gORF") or file.startswith("tORF"):
            #     print(file.startswith("gORF") and file.startswith("tORF"))
                cmd = f'cp {mtb_folder}/{folder}/{file} {outdir}/{folder}/{file}'
                os.system(cmd)


if __name__ == '__main__':
    smorf_gatherer(mtb_folder='/home/adriana/tcc/smorfs/ortho_input_files/smorf_species_based',
                   outdir='/home/adriana/tcc/smorfs/ortho_input_files/final_input_files')
                   # outdir='/home/adriana/PycharmProjects/tcc/scripts/outdir_test')