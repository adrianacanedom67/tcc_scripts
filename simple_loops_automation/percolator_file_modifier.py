"""this script is to modify the percolator raw output files in order to read them with pandas"""

import pandas as pd
import codecs
import os


def file_modificator(folder, outdir):
    files = os.listdir(folder)
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    for file in files:
        with open(f'{folder}/{file}', "r") as f_input, open(f'{outdir}/{file}', "w") as f_output:
            lines = f_input.readlines()
            for line in lines:
                columns = line.strip().split("\t")
                untouched_columns = columns[:4]
                untouched_columns = '\t'.join(untouched_columns)
                print(type(untouched_columns))
                # if columns == columns[5:]:
                merged_columns = ";".join(columns[5:])
                # print(type(merged_columns))

                # modified_data = untouched_columns + "\t" + merged_columns
                # print(modified_data)

            # f_output.write(modified_data + '\n')
                f_output.write(untouched_columns + "\t" + merged_columns + "\n")



        # f_output.write(merged_data + "\n")
if __name__ == '__main__':
    file_modificator(folder='/home/adriana/tcc/smorfs/percolator/transcriptome/raw',
                     outdir='/home/adriana/tcc/smorfs/percolator/transcriptome/modified')
