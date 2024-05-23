import os


"""this script will be to create the txt files to then download the proteomes according to each smorf for orthofinder"""

def proteome_gatherer(folder, outdir):

    subfolders = os.listdir(folder)

    species = []

    for subfolder in subfolders:
        files = os.listdir(f'{folder}/{subfolder}')
        for file in files:
            if not file.startswith("gORF") or not file.startswith("tORF"):
                filename = file.split("_")
                if file.startswith('NC') or file.startswith('NZ'):
                    species_names = filename[2:]
                else:
                    species_names = filename

                species_names = ' '.join(species_names)
                species_names = species_names.replace(".fasta", "").replace("(1)", "")

                if species_names not in species:
                    if not species_names.startswith("gORF"):
                        if not species_names.startswith("tORF"):
                            species.append(f'{species_names}\n')
                # print(species_names)


    species = sorted(set(species))
    # species = list(dict.fromkeys(species))
    # print(species)

        # for smorf in folder:
            # print(smorf)
    with open(f'{outdir}/full_species_list_o.txt', 'w') as outfile:
        outfile.writelines(species)


if __name__ == '__main__':
    proteome_gatherer(folder='/home/adriana/tcc/smorfs/ortho_input_files/without_repeated_species', outdir='/home/adriana/tcc/smorfs/ortho_input_files/species_list_for_proteome')
