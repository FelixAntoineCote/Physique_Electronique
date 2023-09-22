import os
import lvm_read
import matplotlib.pyplot as plt
import numpy as np


#Les histogrammes sans les résistances
liste_fich = os.listdir("Lab_1/Données/Histogrammes")
liste_fich.remove("Résistances")
for fichier in liste_fich:
    #On ouvre chacun des fichiers
    print(fichier)
    lvm = lvm_read.read(f"Lab_1/Données/Histogrammes/{fichier}", dump_file=False)
    
    #On va chercher les informations de l'histogramme avec numpy
    counts, bins = np.histogram(lvm[0]['data'])

    #On plot les données
    plt.stairs(counts, bins, fill=True)
    plt.xlabel("Potentiel [V]")

    #On enregistre les figures avant de les clear
    plt.savefig(f"Lab_1/Figures/Histogrammes/{fichier}.png")
    plt.clf()


#Les histogrammes avec les résistances
liste_fich = os.listdir("Lab_1/Données/Histogrammes/Résistances")
for fichier in liste_fich:
    #On ouvre chacun des fichiers
    print(fichier)
    lvm = lvm_read.read(f"Lab_1/Données/Histogrammes/Résistances/{fichier}", dump_file=False)

    #On plot les données
    plt.hist(lvm[0]['data'])
    plt.xlabel("Potentiel [V]")

    #On enregistre les figures avant de les clear
    plt.savefig(f"Lab_1/Figures/Histogrammes/{fichier}.png")
    plt.clf()