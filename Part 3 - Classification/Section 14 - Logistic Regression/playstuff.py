# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 20:25:31 2018

@author: Thineth
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors

x = np.linspace(-3,3)
X,Y = np.meshgrid(x,x)
Z = np.exp(-(X**2+Y**2))
fig, (ax, ax2) = plt.subplots(ncols=2)

colors=["red", "blue"]

ax.set_title("contour with color list")
contour = ax.contourf(X,Y,Z, colors=colors)

ax2.set_title("contour with colormap")
cmap = matplotlib.colors.ListedColormap(colors)
contour = ax2.contourf(X,Y,Z, cmap=cmap)
fig.colorbar(contour)

plt.show()