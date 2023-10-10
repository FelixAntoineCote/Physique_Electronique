import lvm_read
import matplotlib.pyplot as plt
import numpy as np

#On ouvre le fichier de données
diode_std = lvm_read.read(f"Lab_3/Données/diode.lvm", dump_file=False)
diode_zener = lvm_read.read(f"Lab_3/Données/diode_zener.lvm", dump_file=False)
diode_std_inverse = lvm_read.read(f"Lab_3/Données/diode_inverse.lvm", dump_file=False)

#Toutes les données sont bout à bout, donc on les sépare en 6 et on les plots
data_std = diode_std[0]['data']
X_std = data_std[:, 0]
Y_std = data_std[:, 1]
plt.plot(X_std, Y_std, label="Standard")

data_zener = diode_zener[0]['data']
X_zener = data_zener[:, 0]
Y_zener = data_zener[:, 1]
plt.plot(X_zener, Y_zener, label="Zener")
    
data_std_inverse = diode_std_inverse[0]['data']
X_std_inverse = data_std_inverse[:, 0]
Y_std_inverse = data_std_inverse[:, 1]
plt.plot(X_std_inverse, Y_std_inverse, label="Standard inverse")

plt.legend()
plt.xlabel("Potentiel [V]")
plt.ylabel("Courant [A]")
plt.savefig("Lab_3/Graphiques/Graphique_diodes")