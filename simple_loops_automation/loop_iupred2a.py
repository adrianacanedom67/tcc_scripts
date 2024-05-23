import os
import sys


from Bio import SeqIO

def loop_iupred(file, outdir):

    if not os.path.exists(outdir):
        os.mkdir(outdir)


    records = SeqIO.parse(file, 'fasta')
    for record in records:
        aa_sequence = str(record.seq)
        sequence_name = str(record.description)

        cmd = f'python3 iupred2a.py -a {file}/{record}/{aa_sequence} short'
        os.system(cmd)

        with open(f'{outdir}/{record}/{sequence_name}', 'w') as outfile:
            outfile.writelines()

# haven't tested it yet




if __name__ == '__main__':
    loop_iupred(file='/home/adriana/tcc/smorfs/sequences/sequences_for_idps/smorfs_T1.fasta', outdir='/home/adriana/tcc/smorfs/IUPred2A/short')