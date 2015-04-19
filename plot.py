import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def showImage(zvals):
  cmap = mpl.colors.LinearSegmentedColormap.from_list('my_colormap',['blue','black','red'],256)
  img = plt.imshow(zvals,interpolation='nearest',cmap = cmap,origin='lower')
  plt.colorbar(img,cmap=cmap)
  plt.show()

showImage(np.load('array.npy'))
