import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from numpy.random import randn
import matplotlib.colors as mcolors

def make_colormap(seq):
    """Return a LinearSegmentedColormap
    seq: a sequence of floats and RGB-tuples. The floats should be increasing
    and in the interval (0,1).
    """
    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
        if isinstance(item, float):
            r1, g1, b1 = seq[i - 1]
            r2, g2, b2 = seq[i + 1]
            cdict['red'].append([item, r1, r2])
            cdict['green'].append([item, g1, g2])
            cdict['blue'].append([item, b1, b2])
    return mcolors.LinearSegmentedColormap('CustomMap', cdict)


c = mcolors.ColorConverter().to_rgb
rvb = make_colormap(
    [c('black'),  0.33,  c('red'), 0.66, c('green')])

# Make plot with vertical (default) colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), 0, 3)

cax = ax.imshow(data, interpolation='nearest', cmap=rvb)
ax.set_title('Gaussian noise with vertical colorbar')

# Add colorbar, make sure to specify tick locations to match desired ticklabels
cbar = fig.colorbar(cax, ticks=[0, 1, 2,3,4,5])
cbar.ax.set_yticklabels(['Burnt','Burning','Unburnt'])  # vertically oriented colorbar

# Make plot with horizontal colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), 0, 6)

cax = ax.imshow(data, interpolation='nearest', cmap='gist_earth')
ax.set_title('Gaussian noise with horizontal colorbar')

cbar = fig.colorbar(cax, ticks=[0, 1, 2,3,4,5 ], orientation='vertical')
cbar.ax.set_yticklabels(['Grass', 'Juvenile Pine','Adult Pine','Juvenile hardwood','Adult hardwood'])  # horizontal colorbar

plt.show()