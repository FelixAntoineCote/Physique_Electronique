import pandas as pd
import matplotlib.pyplot as plt
import os

folder = os.listdir("Lab_5/Données")

for i in folder:
    data = pd.read_csv(f"Lab_5/Données/{i}", index_col=0)
    plt.plot(data["Volt_1"], label="Canal 1")
    plt.plot(data["Volt_2"], label="Canal 2 (Sortie)")
    plt.xlabel("Temps [s]")
    plt.ylabel("Potentiel [V]")
    plt.legend()
    plt.savefig(f"Lab_5/Figures/{i[:-4]}.png")
    plt.show()
