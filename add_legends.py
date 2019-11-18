import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 9, 50)

y = x ** 3

z = x ** 2

figure = plt.figure()

axes = figure.add_axes([0,0,1,1])

axes.plot(x, z, label="Square Function")
axes.plot(x, y, label="Cube Function")
axes.legend(loc=4)
plt.show()
