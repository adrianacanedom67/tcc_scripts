import os

# import pandas as pd


"""script to iterate over the orthologue output files in orthofinder to gather all orthologues and give a tsv ouput"""

def orthologue_gatherer(folder, outdir):
    smorf_folders = os.listdir(folder)

    for smorf_folder in smorf_folders:
        ortho_folders = os.listdir(f'{folder}/{smorf_folder}')
        for ortho_folder in ortho_folders:
            result_folders = os.listdir(f'{folder}/{smorf_folder}/{ortho_folder}')
            for result_folder in result_folders:
                main_folders = os.listdir(f'{folder}/{smorf_folder}/{ortho_folder}/{result_folder}')
                # print(main_folders)
                for another_result_folder in main_folders:
                    orthologue_folders = os.listdir(f'{folder}/{smorf_folder}/{ortho_folder}/{result_folder}/{another_result_folder}/Orthologuesx')
                    # print(orthologue_folders)
                    for orthologue_folder in orthologue_folders:
                        if orthologue_folder.startswith("Ortho"):
                            # print(orthologue_folder)
                            orthologue_directory = os.listdir(f'{folder}/{smorf_folder}/{ortho_folder}/{result_folder}/{another_result_folder}/{orthologue_folder}')
                            # print(orthologue_directory)
                            for orthologue_result in orthologue_directory:
                                if orthologue_result.startswith("Ortho"):
                                    final_directory = os.listdir(f'{folder}/{smorf_folder}/{ortho_folder}/{result_folder}/{another_result_folder}/{orthologue_folder}/{orthologue_result}')
                                    print(final_directory)






    if not os.path.exists(outdir):
        os.mkdir(outdir)


if __name__ == '__main__':
    orthologue_gatherer(folder='/home/adriana/tcc/smorfs/orthofinder_first_results', outdir='/home/adriana/tcc/smorfs/orthologues_results')