import lvm_read
import numpy as np
import os

#Les histogrammes avec les résistances
liste_fich = os.listdir("Lab_1/Données/Histogrammes/Résistances")
for fichier in liste_fich:
    #On ouvre chacun des fichiers
    print(fichier)
    lvm = lvm_read.read(f"Lab_1/Données/Histogrammes/Résistances/{fichier}", dump_file=False)

    V = lvm[0]['data'][:,0]
    I = lvm[0]['data'][:,1]

    R = V/I
    moyenne = np.average(R)
    mediane = np.median(R)
    print(f"Valeur de la résistance: {moyenne} ohms avec médiane de {mediane}")