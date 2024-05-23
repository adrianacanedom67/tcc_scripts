import os


def proteome_down(file, outdir):
    with open(file, 'r') as handler:
        lines = handler.readlines()

        for line in lines:
            line = line.rstrip()
            line = line.replace("_", " ")
            print(line)

            cmd = f'ncbi-genome-download --genera "{line}" --formats protein-fasta bacteria --output-folder {outdir} --flat-output'
            os.system(cmd)

if __name__ == '__main__':
    proteome_down(file='/home/adriana/tcc/smorfs/ortho_input_files/species_list_for_proteome/missing_proteomes.txt', outdir='/home/adriana/tcc/smorfs/ortho_input_files/ncbi_gen_down_missing')