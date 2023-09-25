import lvm_read
import numpy as np
import os

#Les histogrammes avec les résistances
liste_fich = os.listdir("Lab_1/Données/Histogrammes/Résistances")
for fichier in liste_fich:
    #On ouvre chacun des fichiers
    lvm = lvm_read.read(f"Lab_1/Données/Histogrammes/Résistances/{fichier}", dump_file=False)

    V_1 = lvm[0]['data'][:,0]
    V_2 = lvm[0]['data'][:,1]

    I = V_2/12
    R = V_1/I
    moyenne = np.average(R)
    mediane = np.median(R)
    omega = 3*np.std(R)
    print(f"Valeur de la résistance: {moyenne} ohms avec une médiane de {mediane} et un écart-type de {omega}\n")