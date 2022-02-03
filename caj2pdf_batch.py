import os

def caj_list(file_dir):
    flist = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.caj':
                flist.append(os.path.splitext(file)[0])
    return flist

fdir = './caj_to_convert/'
outdir = './output_pdfs/'
flist = caj_list(fdir)

for fname in flist:
    cmd = "./caj2pdf convert " + fdir + fname + ".caj" + " -o " + outdir + fname + ".pdf"
    print(cmd)
    os.system(cmd)
