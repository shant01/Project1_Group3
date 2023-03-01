import os
import glob
import numpy as np
import matplotlib.pyplot as plt

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

NRenergies.close()
OEenergies.close()
TEenergies.close()

NRenergies_table = np.loadtxt("NRenergies.txt")

print('NRenergies_table')
for each in NRenergies_table:
    print(each)
print('\n')
    
OEenergies_table = np.loadtxt("OEenergies.txt")

print('OEenergies_table')
for each in OEenergies_table:
    print(each)
print('\n')

TEenergies_table = np.loadtxt("TEenergies.txt")

print('TEenergies_table')
for each in TEenergies_table:
    print(each)
print('\n')



#create three subplots
fig, axs = plt.subplots(3)

# Plot NRenergies
axs[0].plot(NRenergies_table)
axs[0].set_title('Nuclear Repulsion Energy')

# Plot OEnergies
axs[1].plot(OEenergies_table)
axs[1].set_title('One-electron Energy')

# Plot TEnergies
axs[2].plot(TEenergies_table)
axs[2].set_title('Two-electron Energy')

# Set common x and y labels for all subplots
fig.text(0.5, 0.05, 'Index', ha='center')
fig.text(0.05, 0.5, 'Energy', va='center', rotation='vertical')


plt.show()