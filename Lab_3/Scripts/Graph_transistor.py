import lvm_read
import matplotlib.pyplot as plt
import numpy as np

#On ouvre le fichier de données
lvm = lvm_read.read(f"Lab_3/Données/transistor.lvm", dump_file=False)

#Toutes les données sont bout à bout, donc on les sépare en 6 et on les plots
for i in range(6):
    data = lvm[0]['data'][i*20:(i+1)*20]
    X = data[:, 0]
    Y = data[:, 1]
    if i == 0:
        plt.plot(X, Y, label=f"I_sat = (0 ± 0.0001) A")
    if i == 1:
        plt.plot(X, Y, label=f"I_sat = (0 ± 0.0001) A")
    if i == 2:
        plt.plot(X, Y, label=f"I_sat = (0 ± 0.0001) A")
    if i == 3:
        plt.plot(X, Y, label=f"I_sat = (0.0007 ± 0.0001) A")
    if i == 4:
        plt.plot(X, Y, label=f"I_sat = (0.1000 ± 0.0006) A")
    if i == 5:
        plt.plot(X, Y, label=f"I_sat = (0.300 ± 0.002) A")
    

plt.legend()
plt.xlabel("Potentiel [V]")
plt.ylabel("Courant [A]")
plt.savefig("Lab_3/Graphique_transistor.png")