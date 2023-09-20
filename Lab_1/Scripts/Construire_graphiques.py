import os
import lvm_read
import matplotlib.pyplot as plt

#On va chercher tous les noms fichiers de données à Scatter
liste_fich = os.listdir("Lab_1/Données/Scatter")


for fichier in liste_fich:
    #On ouvre chacun des fichiers
    print(fichier)
    lvm = lvm_read.read(f"Lab_1/Données/Scatter/{fichier}", dump_file=False)
    plt.plot(lvm[0]['data'], marker='.')
    plt.ylabel("Potentiel [V]")
    plt.xlabel("Temps [s]")
    plt.legend(fichier)
    plt.show()