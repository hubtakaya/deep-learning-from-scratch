import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def func(x):
    return x[0]**2 + x[1]**2

x = [0, 0]
x[0] = np.arange(-5, 5, 0.25)
x[1] = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(x[0], x[1])

x[0] = X
x[1] = Y
Z = func(x)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(x[0],x[1],Z)
plt.show()

