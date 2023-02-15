# if we don't specify the points on the x-axis , they
# will get the default values 0,1,2,3...
# depending on the length of the y-points

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([1,5,7,9,19,8])

plt.plot(ypoints)
plt.show()