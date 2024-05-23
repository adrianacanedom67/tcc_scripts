import os


from Bio import SeqIO

"""this script will be used to separate all the IDPs regarding their AA length"""

smaller_proteins = {}   #this dictionary will contain those orfs from 20-50AA
larger_proteins = {}    #this dictionary will contain those orfs from 50-99AA


def idp_isolator(file, outdir):
    records = SeqIO.parse(f'{file}', 'fasta')
    for record in records:
        orf_name = str(record.description)
        orf_seq = str(record.seq)
        # print(orf_name)
        # print(orf_seq)
        if len(orf_seq) >= 50:
            if orf_name not in larger_proteins:
                larger_proteins[f'>{orf_name}\n'] = []
            if orf_seq not in larger_proteins[f'>{orf_name}\n']:
                larger_proteins[f'>{orf_name}\n'].append(f'{orf_seq}\n')
                # print(larger_proteins)

        if len(orf_seq) <=50 and len(orf_seq) >=20:
            if orf_name not in smaller_proteins:
                smaller_proteins[f'>{orf_name}\n'] = []
            if orf_seq not in smaller_proteins[f'>{orf_name}\n']:
                smaller_proteins[f'>{orf_name}\n'].append(f'{orf_seq}\n')
                print(smaller_proteins)

        if not os.path.exists(outdir):
            os.mkdir(outdir)


        with open(f'{outdir}/larger_idps.fasta', 'w') as outfile:
            outfile.writelines(larger_proteins)

        with open(f'{outdir}/smaller_idps.fasta', 'w') as outfile:
            outfile.writelines(smaller_proteins)

if __name__ == '__main__':
    idp_isolator(file='/home/adriana/tcc/smorfs/sequences/sequences_for_idps/smorfs_t1.fasta',
                 outdir='/home/adriana/tcc/smorfs/sequences/sequences_for_idps/filtered')