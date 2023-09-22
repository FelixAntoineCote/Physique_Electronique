import os
import lvm_read
import matplotlib.pyplot as plt

#On va chercher tous les noms fichiers de données à Scatter
liste_fich = os.listdir("Lab_1/Données/Histogrammes")


for fichier in liste_fich:
    #On ouvre chacun des fichiers
    print(fichier)
    lvm = lvm_read.read(f"Lab_1/Données/Histogrammes/{fichier}", dump_file=False)
    plt.hist(lvm[0]['data'])
    plt.ylabel("Potentiel [V]")
    plt.xlabel("Temps [1/10s]")
    plt.savefig(f"Lab_1/Figures/Histogrammes/{fichier}.png")
    plt.clf()