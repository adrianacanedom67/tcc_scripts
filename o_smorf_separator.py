import os

from Bio import SeqIO

"""this scrip is to choose the largest protein among those (orthologues) with the same stop codon in the 
blastp results from smorfs with other organisms"""

def o_smorf_gatherer(folder, outdir):
    files = os.listdir(folder)

    for file in files:
        print(file)
        all_orfs = {}
        records = SeqIO.parse(f'{folder}/{file}', 'fasta')
        for record in records:
            identifier = record.description
            if identifier.startswith(" ORF"):
                # print(identifier)
                identifier_parts = identifier.split('_')
                # print(identifier_parts)
                species_strain = '_'.join(identifier_parts[-4:])
                # print(species_strain)
                coordinates = identifier_parts[5]
                codon = coordinates.split('-')
                # print(codon)
                stop_codon = codon[-1]
                # print(stop_codon)
                length = identifier_parts[3]
                # print(length)
                if species_strain not in all_orfs:
                    all_orfs[species_strain] = {}
                if stop_codon not in all_orfs[species_strain]:
                    all_orfs[species_strain][stop_codon] = {}
                if length not in all_orfs[species_strain][stop_codon]:
                    all_orfs[species_strain][stop_codon][length] = {}
                if identifier not in all_orfs[species_strain][stop_codon][length]:
                    all_orfs[species_strain][stop_codon][length] = identifier
                # print(all_orfs)


            unique_orfs_list = []

            for species_strain in all_orfs:
                for stop_codon in all_orfs[species_strain]:
                    biggest_orf = max(all_orfs[species_strain][stop_codon])
                    # print(all_orfs)
                    # print(all_orfs[species_strain][stop_codon][biggest_orf])
                    # print(all_orfs[species_strain][stop_codon][biggest_orf])
                    unique_orfs = all_orfs[species_strain][stop_codon][biggest_orf]
                    # print("unique orfs:", unique_orfs)
                    # print(type(unique_orfs))
                    unique_orfs_list.append(f'>{unique_orfs}\n')
            print(unique_orfs_list)

                # print(all_orfs[species_strain][stop_codon])
                # print(stop_codon)


            # print("____________________")
            with open(f'{outdir}/{file}', 'w') as outfile:
                outfile.writelines(unique_orfs_list)




if __name__ == '__main__':
    o_smorf_gatherer(folder='/home/adriana/tcc/smorfs/orthofinder_first_results/orthologues',
                     outdir='/home/adriana/tcc/smorfs/orthofinder_first_results/orthologues_unrepeated')