import numpy as np
import matplotlib.pyplot as plt
import math as mt
from matplotlib.animation import FuncAnimation as fa
import tensorflow as tf

r = 8           # the raduis of 3d-sphere
db = 3          # The distance between the boundary 3d-sphere and the edge of the 3d-space
dist = .3       # The distance between 2d-circles
scaler = 100    # The scaller of cardinality of the set [0, 2pi]
xc = 0          # x coordinaite
yc = 0          # y coordinaite
zc = 0          # z coordinaite

plt.style.use('dark_background')
fig = plt.figure()
ax = fig.add_subplot(projection='3d', aspect='equal')
ax.axis('off')
ax.set_facecolor('black')
ax.set(xlim=[-(r+db), r+db], ylim=[-(r+db), r+db], zlim=[-(r+db), r+db])
a = np.linspace(0, 2*np.pi, mt.ceil(2*np.pi*scaler))

S = []
i = -r
while i < r+dist:
    ax.plot((np.sqrt(r**2-(i-xc)**2)+yc)*np.cos(a), (np.sqrt(r**2-(i-yc)**2)+yc)*np.sin(a), [i]*len(a), color=[1/2, 1/4, 1/16, .9][::-1])
    point, = ax.plot([], [], [], marker='.', color='white')
    S.append(point)
    i += dist

def init():
    for sca in S:
        sca.set_data([], [])
        sca.set_3d_properties([])
    return S

z = np.arange(-r, r+dist, dist)

def rotation(_):
    for sca, i in zip(S, z):
        x, y = (np.sqrt(r**2-(i-xc)**2)+yc)*np.cos(_/(np.sqrt(r**2-(i-xc)**2)+yc)), (np.sqrt(r**2-(i-yc)**2)+xc)*np.sin(_/(np.sqrt(r**2-(i-yc)**2)+xc))
        sca.set_data([x], [y])
        sca.set_3d_properties([i])
    return S
    
ax.view_init(azim=30, elev=20)
plt.tight_layout()
p = 6
anim = fa(fig, init_func=init, func=rotation, frames=np.concatenate([np.linspace(p*np.pi, (p+1)*np.pi, mt.ceil(np.pi*(2+1/(1+np.exp(p))))) for p in range(-20, 100)], axis=0),
           interval=0, blit=False)
plt.show()
#plt.savefig(r'C:\users\azahr\Music\plot.png', dpi=300)
