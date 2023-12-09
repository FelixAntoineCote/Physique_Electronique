import matplotlib.pyplot as plt

X = [5, 10, 15, 23]
Y = [240, 366, 435, 495]

plt.plot(X, Y)
plt.xlabel("v_motor")
plt.ylabel("Vitesse du moteur [RPM]")
plt.show()