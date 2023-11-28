import matplotlib.pyplot as plt
import lvm_read as lvm
import numpy as np

data = lvm.read("C:/BAC PHY/Physique_Electronique/Atelier_1/Données/4d.lvm", dump_file=False)

y = 20*np.log(data[0]["data"][:11, 2]/data[0]["data"][:11, 1])
x = 2**data[0]["data"][:11, 0]

print(data[0]["data"][:, 2]/data[0]["data"][:, 1])

plt.plot(x, y)
plt.xlabel("Fréquence [Hz]")
plt.ylabel("Décibel (dB)")
plt.xscale("log")
plt.savefig("C:/BAC PHY/Physique_Electronique/Atelier_1/Graph_4d")

