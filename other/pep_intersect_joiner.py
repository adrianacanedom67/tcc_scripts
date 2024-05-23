"""to join both the genome and transcriptome lists of intersection peps (those peptides that matched with
the reference proteome) excluding repeated lines"""

import pandas as pd
df1 = pd.read_csv('/home/adriana/tcc/smorfs/percolator/transcriptome/Intersections/intersection_peps.csv', delimiter='\t')
df2 = pd.read_csv('/home/adriana/tcc/smorfs/percolator/genome/Intersections/intersection_peps.csv', delimiter='\t')

merged_df = pd.merge(df1, df2, on='proteinIds',how='outer')
merged_df = merged_df.drop_duplicates()
merged_df.to_csv('/home/adriana/tcc/smorfs/percolator/merged_peps_intersections.csv', index=False)