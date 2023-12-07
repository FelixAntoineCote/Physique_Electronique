import numpy as np
import matplotlib.pyplot as plt

f = np.linspace(1, 15000000, 10000000)*2*np.pi
y_2 = np.absolute((10**6/(6j*f) + (10**6+270j*f)/(135j*f) + (12*(10**6+270j*f))/(270*10**6)+2)**(-1))

y_1 = ((1j*f)**2 + 10**9)/(1.27*((1j*f)**2 + 10**9) + 270*1j*f*10**3)

y_1_gain = np.absolute(y_1)

y_1_phase = np.arctan(np.imag(y_1)/np.real(y_1))



plt.plot(f, y_1_gain)
plt.xscale("log")
plt.xlabel("Fréquence [Hz]")
plt.ylabel("Gain [-]")
plt.plot(7500, 0.4, marker="o", label="7500 Hz")
plt.plot(126000, 0.4, marker="o", label="126000 Hz")
plt.legend()
plt.show()