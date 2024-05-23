"""this script, once percolator raw output files have been modified, is to filter out the results with a q-value > 0.01"""

import os
import pandas as pd

def percolator_filter(qvalue_cutoff = 0.01):
    # passed_cutoffs = {} # this dictionary will contain those lines that surpass the q-value

    print(os.getcwd())
    df = pd.read_csv(f'/home/adriana/tcc/smorfs/percolator/transcriptome/modified/pep_results.csv', low_memory=True)
    print(df)
    print(f'{df["q-value"][0]} - {type(df["q-value"][0])}')

    df["q-value"] = df["q-value"]
    wanted_qvalues = df.loc[df["q-value"] < qvalue_cutoff]
    return

        # wanted_qvalues.to_csv(f'{outdir}/{file}', sep='\t', index=False)
        # print(f"Successfully created f'{file}'")

if __name__ == '__main__':
    percolator_filter()
