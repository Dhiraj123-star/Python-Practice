# Plotting without line
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,4])
ypoints= np.array([1,70])

plt.plot(xpoints,ypoints,'o')
plt.show()