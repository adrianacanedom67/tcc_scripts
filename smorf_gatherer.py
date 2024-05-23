import os

from Bio import SeqIO

def comp_smorf_gatherer(blastp_folder, osmorf_folder, outdir):

    blastp_files = os.listdir(blastp_folder)
    complete_protein_names = {}   # key, value: smorf, [id1, id2, id3...]
    mtb_smorfs_seqs = {}

    for file in blastp_files:
        if file.endswith('fasta'):
            records = SeqIO.parse(f'{blastp_folder}/{file}', 'fasta')
            i = 0
            for record in records:
                identifiers = str(record.description)
                # print(identifiers)
                if file not in complete_protein_names:
                    complete_protein_names[file] = []
                if identifiers not in complete_protein_names[file]:
                    complete_protein_names[file].append(identifiers)
                if i == 0:
                    mtb_smorfs_seqs[str(record.description)] = str(record.seq)
                i += 1

    # print(complete_protein_names)

    osmorf_files = os.listdir(osmorf_folder)

    smorf_hits_final_files = {}

    for other_file in osmorf_files:
        if other_file.endswith('fasta'):
            for smorf in complete_protein_names:

                if smorf not in smorf_hits_final_files:
                    smorf_hits_final_files[smorf] = []
                    if smorf.startswith("gORF") or smorf.startswith("tORF"):
                        # print(mtb_smorfs_seqs[smorf])
                        smorf_hits_final_files[smorf].append(f'>{smorf.replace(".fasta", "")}\n{mtb_smorfs_seqs[smorf.replace(".fasta", "")]}\n')
                records = SeqIO.parse(f'{osmorf_folder}/{other_file}', 'fasta')
                for record in records:
                    if str(record.description) in complete_protein_names[smorf]:
                        smorf_hits_final_files[smorf].append(f'>{str(record.description)}\n{str(record.seq)}\n')
    print(smorf_hits_final_files)

    for mtb_smorfs in smorf_hits_final_files:
        with open (f'{outdir}/{mtb_smorfs}.fasta', 'w') as outfile:
            outfile.writelines(smorf_hits_final_files[mtb_smorfs])

if __name__ == '__main__':
    # comp_smorf_gatherer(blastp_folder='/home/farminfo/PycharmProjects/ACanedo/scripts/folder', osmorf_folder='/home/farminfo/PycharmProjects/ACanedo/scripts/folder/o_smorfs_test', outdir='/home/farminfo/PycharmProjects/ACanedo/scripts/outdir')
    comp_smorf_gatherer(blastp_folder='/home/farminfo/ACanedo/blastp_parsed_smorfs/full_protein_name', osmorf_folder='/home/farminfo/ACanedo/new_smorfs', outdir='/home/farminfo/ACanedo/blastp_parsed_smorfs/full_name_sequence')