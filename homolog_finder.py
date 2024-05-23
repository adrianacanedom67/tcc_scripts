import os

from Bio import SeqIO

"""this script is to gather the homolog smorfs found in the blastp based on the same stop codon,
then I'll choose the longest sequence (which is already included in the identifier)"""

def homolog_finder(folder, outdir):
    files = os.listdir(folder)

    for file in files:
        records = SeqIO.parse(f'{folder}/{file}', 'fasta')
        unrepeated_o_smorfs = {}
        complete_dictionary = {}

        for record in records:
            identifiers = str(record.description)
            # print(identifiers)
            sequence = str(record.seq)
            if identifiers.startswith("gORF") or identifiers.startswith("tORF"):
                mtb_smorf = identifiers
                print(mtb_smorf)
                mtb_seq = sequence
            if not identifiers.startswith("gORF"):
                if not identifiers.startswith("tORF"):
                    # print(identifiers)
                    temporary_names = identifiers.split("_")
                    # print(temporary_names)
                    temp_names_two = identifiers.split('/')
                    species_temp = temp_names_two[-1]
                    print(species_temp)
                    species_names = species_temp
                    # species_names = '_'.join(species_temp)
                    if species_names.startswith("smorfs"):
                        # smorf_sp_n = species_names.split("/")  #this variable is for those that start with "smorf/" in the genera name
                        # species_names = smorf_sp_n[-1]
                        smorf_sp_n = species_names.replace("smorfs/", "")
                        species_names = smorf_sp_n
                        corrected_names = species_names.replace("[", "").replace("]", "") #this variable will remove [] for those genera that start with square brackets
                        species_names = corrected_names
                    # print("species:", species_names)
                    coordinates = temporary_names[5]
                    # print(coordinates)
                    codon = coordinates.split("-")
                    # print(codon)
                    start_codon = codon[0]
                    stop_codon = codon[1]
                    # print("stop_codon:", stop_codon)
                    sequence_length = len(str(record.seq))
                    # print("length:", sequence_length)
                    orf_temp_name = temporary_names[:2]
                    # print(orf_temp_name)
                    # orf_name = '_'.join(orf_temp_name)
                    orf_name = identifiers
                    # print(orf_name)
                    complete_dictionary[orf_name] = str(record.seq)


                    if species_names not in unrepeated_o_smorfs:
                        unrepeated_o_smorfs[species_names] = {}
                    if stop_codon not in unrepeated_o_smorfs:
                        unrepeated_o_smorfs[species_names][stop_codon] = {}
                    if start_codon not in unrepeated_o_smorfs[species_names][stop_codon]:
                        unrepeated_o_smorfs[species_names][stop_codon][start_codon] = {}


                    unrepeated_o_smorfs[species_names][stop_codon][start_codon]['len'] = sequence_length
                    unrepeated_o_smorfs[species_names][stop_codon][start_codon]['name'] = orf_name
                    unrepeated_o_smorfs[species_names][stop_codon][start_codon]['seq'] = str(record.seq)
                    # print(unrepeated_o_smorfs)
        to_write = [f'>{mtb_smorf}\n{mtb_seq}\n']

        for species in unrepeated_o_smorfs:
            # print(type(species))
            print(orf_name)

            for stop_codon in unrepeated_o_smorfs[species]:
                longest_orf = None
                longest_seq = 0
                chosen_Seq = None
                print(species, stop_codon)
                for start_codon in unrepeated_o_smorfs[species][stop_codon]:
                    print(longest_seq)
                    sequence_length = unrepeated_o_smorfs[species][stop_codon][start_codon]['len']
                    # print(type(sequence_length))
                    print(type(longest_seq))
                    if sequence_length > longest_seq: #essa merda tá pegando a menor
                        longest_seq = sequence_length
                        print(longest_seq)
                        print(sequence_length)
                        # longest_orf = orf_name
                        longest_orf = unrepeated_o_smorfs[species][stop_codon][start_codon]['name']
                        chosen_Seq = unrepeated_o_smorfs[species][stop_codon][start_codon]['seq']
                print('\n')
            # seq = complete_dictionary[longest_orf]
                to_write.append(f'>{longest_orf}\n{chosen_Seq}\n')

            dictio = {'m_tuberculosis': {12323: {12000: {'len': 34, 'name': 'gorf223_dsdsjdi_53535_sdsd', 'seq': 'ASUHSUAHSUADHS'}}}}

                    # print(unrepeated_o_smorfs)
                    #             print("species:", species_names)
                    #             print("corresponding stop codon:", stop_codon)
                    #             print("longest orf:", longest_orf)
                    #             print("longest sequence length:", longest_seq)

            # if identifiers in unrepeated_o_smorfs:
        with open(f'{outdir}/{file}.fasta', 'w') as outfile:
            outfile.writelines(to_write)





if __name__ == '__main__':
    homolog_finder(folder='/home/farminfo/ACanedo/blastp_parsed_smorfs/full_name_sequence', outdir='/home/farminfo/PycharmProjects/ACanedo/scripts/outdir')
