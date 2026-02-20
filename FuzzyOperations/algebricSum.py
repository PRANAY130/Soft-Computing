import numpy as np
import matplotlib.pyplot as plt

def triangular_mf(x, a, b, c):
    return np.maximum(0, np.minimum((x-a)/(b-a), (c-x)/(c-b)))

x = np.linspace(0, 10, 1000)

setA = triangular_mf(x, 1, 3, 5)
setB = triangular_mf(x, 2, 6, 8)
inter = np.minimum(setA, setB)

alg_sum = (setA + setB) - inter

plt.plot(x, setA, label=f"setA", linestyle='dashed')
plt.plot(x, setB, label=f"setB", linestyle='dashed')
plt.plot(x, alg_sum, label=f'alg_sum', linewidth=2)
plt.fill_between(x, alg_sum, color='green', alpha=0.2)
plt.xlabel('x values')
plt.ylabel('Membership Degree')
plt.title('Triangular Membership Function')
plt.legend()
plt.grid()
plt.show()