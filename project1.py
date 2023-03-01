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

NRenergies_table = np.loadtxt('NRenergies.txt')

print('NRenergies_table')
for each in NRenergies_table:
    print(each)
print('\n')

OEenergies_table = np.loadtxt('OEenergies.txt')

print('OEenergies_table')
for each in OEenergies_table:
    print(each)
print('\n')

TEenergies_table = np.loadtxt('TEenergies.txt')

print('TEenergies_table')
for each in TEenergies_table:
    print(each)
print('\n')

fig, axs = plt.subplots(3, figsize=(20,20))

axs[0].plot(NRenergies_table, '--o')
axs[0].set_title('Nuclear Repulsion Energy')
plt.xlabel('Index')
plt.ylabel('Energy')

axs[1].plot(OEenergies_table, '--o')
axs[1].set_title('One-Electron Energy')
plt.xlabel('Index')
plt.ylabel('Energy')

axs[2].plot(TEenergies_table, '--o')
axs[2].set_title('Two-Electron Energy')
plt.xlabel('Index')
plt.ylabel('Energy')

plt.show()

fig, axs = plt.subplots(figsize=(20,20))

axs.plot(NRenergies_table, '--o')
plt.xlabel('Index')
plt.ylabel('Energy')

axs.plot(OEenergies_table, '--o')
plt.xlabel('Index')
plt.ylabel('Energy')

axs.plot(TEenergies_table, '--o')
plt.xlabel('Index')
plt.ylabel('Energy')

plt.legend(['Nuclear Repulsion Energy', 'One-Electron Energy', 'Two-Electron Energy'], bbox_to_anchor = (0.75, 1.00), borderpad = 1, ncol = 3)
plt.show()