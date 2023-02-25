import os
import glob

file_loc = os.path.join('data', 'outfiles', '*.out')

file_names = glob.glob(file_loc)

NRenergies = open('NRenergies.txt', 'w+')
OEenergies = open('OEenergies.txt', 'w+')
TEenergies = open('TEenergies.txt', 'w+')

for f in file_names:
    outfile = open(f, 'r')
    data = outfile.readlines()
    outfile.close()

    for line in data:
        if 'Nuclear Repulsion Energy' in line:
            nre_line = line
            words1 = nre_line.split()
            nre = float(words1[-1])
            NRenergies.write(F'{nre} \n')

        if 'One-Electron Energy' in line:
            oee_line = line
            words2 = oee_line.split()
            oee = float(words2[-1])
            OEenergies.write(F'{oee} \n')

        if 'Two-Electron Energy' in line:
            tee_line = line
            words3 = tee_line.split()
            tee = float(words3[-1])
            TEenergies.write(F'{tee} \n')
            print(tee)

NRenergies.close()
OEenergies.close()
TEenergies.close()

#Generate Tables

#First Code Block
import numpy
file_loc = os.path.join('data', 'outfiles', '*.out')

file_names = glob.glob(file_loc)

NRenergies = open('NRenergies_table', 'w+')
OEenergies = open('OEenergies_table', 'w+')
TEenergies = open('TEenergies_table', 'w+')


#Second Code Block
NRenergies_file = os.path.join('NRenergies.txt')
NRenergies_text = numpy.genfromtxt(fname=NRenergies_file, delimiter = ',', dtype='unicode')
NRenergies.write(F'{NRenergies_text} \n')
print("NRenergies Table:")
print(NRenergies_text)
NRenergies.close()

OEenergies_file = os.path.join('OEenergies.txt')
OEenergies_text = numpy.genfromtxt(fname=OEenergies_file, delimiter = ',', dtype='unicode')
OEenergies.write(F'{OEenergies_text} \n')
OEenergies.close()
print("OEenergies Table:")
print(OEenergies_text)
OEenergies.close()

TEenergies_file = os.path.join('TEenergies.txt')
TEenergies_text = numpy.genfromtxt(fname=TEenergies_file, delimiter = ',', dtype='unicode')
TEenergies.write(F'{TEenergies_text} \n')
TEenergies.close()
print("TEenergies Table:")
print(TEenergies_text)
TEenergies.close()