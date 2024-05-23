"""this script is to gather and filter out the documents I need to send to Eduardo for my IC"""

import os
from Bio import SeqIO
import pandas as pd
import openpyxl


def smorf_names(sequence_folder, interpro_folder):
    smorf_interpro = {}
    sequence_files = os.listdir(sequence_folder)
    for sequence_file in sequence_files:
        records = SeqIO.parse(f'{sequence_folder}/{sequence_file}', 'fasta')
        if sequence_file not in smorf_interpro:
            smorf_interpro[sequence_file] = {}
            for record in records:
                identifier = str(record.description)
                if identifier not in smorf_interpro:
                    smorf_interpro[sequence_file][identifier] = {"domains" : [], "start_coord": [], "stop_coord": []}
                    # print(smorf_interpro)
    interpro_files = os.listdir(interpro_folder)
    for interpro_file in interpro_files:
        # print(interpro_file)
        df = pd.read_csv(f'{interpro_folder}/{interpro_file}', sep='\t')
        # df.columns = df.iloc[0]

        # df = df[1:]
        pd.set_option('display.max_columns', None)
        # print(df)
        # print(df.columns)
        # df2 = df.loc[:, ["smORF_name", "domain ", "start_coord", "stop_coord"]]
        # print(df2)
        for tier in smorf_interpro:
            for identifier in smorf_interpro[tier]:
                print(tier)
                print(identifier)
                print(smorf_interpro[tier][identifier])
                df3 = df[df["smORF_name"] == identifier]
                print(df3)
        # print(df3)
        # for tier in smorf_interpro:
        #     print(tier)
        break


if __name__ == '__main__':

    smorf_names(sequence_folder='/home/adriana/tcc/smorfs/sequences/only_names',
                interpro_folder='/home/adriana/tcc/smorfs/InterPro/until_tier_three')
