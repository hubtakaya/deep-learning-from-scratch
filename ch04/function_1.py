import numpy as np
import matplotlib.pylab as plt
from numerical_diff import numerical_diff

def function_1(x):
    return 0.01*x**2 + 0.1*x

print(numerical_diff(function_1, 5))
print(numerical_diff(function_1, 10))

x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.xlabel("f(x)")
plt.plot(x, y)
plt.show()
