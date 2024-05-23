import os



#this script is to filter out those other bacteria's sequences that are repeated

def sequence_filter(folder, outdir):

    subfolders = os.listdir(folder) #this will be the folder containing the subfolders. Each subfolder is a smORF name


    for subfolder in subfolders:

        # for file in subfolder:
        files = os.listdir(f'{folder}/{subfolder}')  # each file is a species name
        species_file_sizes = {}
        for file in files:
            filename = file.split("_")

            if file.startswith('NC') or file.startswith('NZ'):
                species_names = filename[2:]
            else:
                species_names = filename

            species_names = '_'.join(species_names)

            size = os.stat(f'{folder}/{subfolder}/{file}').st_size
            dictio = {'mtb': {'file1': 1212, 'file2': 2323}}

            if species_names not in species_file_sizes:
                species_file_sizes[species_names] = {}

            species_file_sizes[species_names][file] = size

        for species in species_file_sizes:
            # print(type(species))

            biggest_file = None
            biggest_size = 0

            for file in species_file_sizes[species]:
                ...
                # print(file)
                # for file in species_file_sizes[species]:
                size = species_file_sizes[species][file]
                # print('species:', species)
                # print('file:', file)
                if size > biggest_size:
                    biggest_size = size
                    biggest_file = file

            if not os.path.exists(f'{outdir}/{subfolder}'):
                os.mkdir(f'{outdir}/{subfolder}')


            cmd = f'cp {folder}/{subfolder}/{biggest_file} {outdir}/{subfolder}/{biggest_file}'
            os.system(cmd)


if __name__ == '__main__':
    sequence_filter(folder='/home/farminfo/ACanedo/orthofinder_inputfiles/smorf_species_based', outdir='/home/farminfo/PycharmProjects/ACanedo/scripts/outdir')