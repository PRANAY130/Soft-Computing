import numpy as np
import matplotlib.pyplot as plt

def triangular_mf(x, a, b, c):
    return np.maximum(0, np.minimum((x-a)/(b-a), (c-x)/(c-b)))

x = np.linspace(0, 10, 1000)

setB = triangular_mf(x, 2, 6, 8)

comp = 1 - setB

plt.plot(x, setB, label=f"setB", linestyle='dashed')
plt.plot(x, comp, label=f'Complement', linewidth=2)
plt.xlabel('x values')
plt.ylabel('Membership Degree')
plt.title('Triangular Membership Function')
plt.legend()
plt.grid()
plt.show()