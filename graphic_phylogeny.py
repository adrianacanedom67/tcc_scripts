import os
from Bio import SeqIO
import pandas as pd
import matplotlib.pyplot as plt


"""this script is an attempt to build the graphics comparing homologs and orthologs"""

def bar_graph_maker(homolog_folder, orthologue_folder, outdir):

    smorfs_graph = {}  # this dictionary will store information for the bar graphs



    files = os.listdir(homolog_folder)
    for file in files:
        records = SeqIO.parse(f'{homolog_folder}/{file}', 'fasta')
        for record in records:
            identifiers = str(record.description)
            sequences = str(record.seq)
            if identifiers.startswith("gORF") or identifiers.startswith("tORF"):
                mtb_smorf = identifiers
                # print(type(mtb_smorf))
                # print(mtb_smorf)
                smorfs_graph[mtb_smorf] = {}
                # print(smorfs_graph)
                smorfs_graph[mtb_smorf]["homologues"] = {}
                # print(smorfs_graph)
            n = 0
            for record in records:
                if not identifiers.startswith("gORF") or not identifiers.startswith("tORF"):
                    n += 1
            # print(file, n)
            number_homol = str(n)
            # print(type(number_homol))
            # print(file, number_homol)
            smorfs_graph[mtb_smorf]["homologues"] = number_homol
            # print(smorfs_graph)

        ortho_files = os.listdir(orthologue_folder)
        for ortho_file in ortho_files:
            records = SeqIO.parse(f'{orthologue_folder}/{ortho_file}', 'fasta')
            n = 0
            for record in records:
                identifiers = str(record.description)
                # print(identifiers)
                if identifiers.startswith(" ORF"):
                    n += 1

            number_orthol = str(n)
            # print(ortho_file, "orthologues:", number_orthol)
            # print(smorfs_graph[mtb_smorf]["orthologues"])
            filename = ortho_file.replace(".fasta", "")
            # print(filename)
            if filename == mtb_smorf:
                smorfs_graph[mtb_smorf]["orthologues"] = {}
                smorfs_graph[mtb_smorf]["orthologues"] = number_orthol
    print(smorfs_graph)


    mtb_smorf_list = smorfs_graph.keys()
    print(mtb_smorf_list)


    df = pd.DataFrame(smorfs_graph).T
    print(df)
    # ax = df.plot.hist(column=)
    # matplotlib.pyplot.hist()
    df.hist(column='mtb')



if __name__ == '__main__':
    bar_graph_maker(homolog_folder='/home/adriana/tcc/smorfs/orthofinder_first_results/homologs',
                    orthologue_folder='/home/adriana/tcc/smorfs/orthofinder_first_results/orthologues_unrepeated',
                    outdir='/home/adriana/tcc/smorfs/orthofinder_first_results/graph_test')