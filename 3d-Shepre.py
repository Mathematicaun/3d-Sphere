import numpy as np
import matplotlib.pyplot as plt
import math as mt
from matplotlib.animation import FuncAnimation as fa

r = 50          # the raduis of 3d-sphere
ld = 2        # The distance between 2d-circles
scaler = 100   # The scaller for the cardinality of the closed interval [0, 2pi]
x_max = 100     # The boundary sapce along x-axis
y_max = 100    # The boundary sapce along y-axis
z_max = 100     # The boundary sapce along z-axis
X = 40          # x coordinaite
Y = 40           # y coordinaite
Z = 10          # z coordinaite

if (X+r > x_max or X-r < -x_max) or (Y+r > y_max or Y-r < -y_max) or (Z+r > z_max or Z-r < -z_max):
    print('The 3d-Sphere is out of the Space')
else:
    plt.style.use('dark_background')
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d', aspect='equal')
    ax.axis('on')
    ax.set_facecolor('black')
    ax.set(xlim=[-x_max, x_max], ylim=[-y_max, y_max], zlim=[-z_max, z_max])
    a = np.linspace(0, 2*np.pi, mt.ceil(2*np.pi*scaler))

    ax.plot([X], [Y], [Z], color='blue', marker='.')

    S = []
    i = Z-r

    while i < Z+r+ld:
        ax.plot(np.sqrt(r**2-(i-Z)**2)*np.cos(a)+X, np.sqrt(r**2-(i-Z)**2)*np.sin(a)+Y, [i]*len(a), color=[1/2, 1/4, 1/16, .9][::-1])
        point, = ax.plot([], [], [], marker='.', color='white')
        S.append(point)
        i += ld

    def init():
        for sca in S:
            sca.set_data([], [])
            sca.set_3d_properties([])
        return S

    z = np.arange(Z-r, Z+r+ld, ld)

    def rotation(_):
        for sca, i in zip(S, z):
            x, y = np.sqrt(r**2-(i-Z)**2)*np.cos(_/np.sqrt(r**2-i**2))+X, np.sqrt(r**2-(i-Z)**2)*np.sin(_/np.sqrt(r**2-i**2))+Y
            sca.set_data([x], [y])
            sca.set_3d_properties([i])
        return S
        
    ax.view_init(azim=30, elev=20)
    plt.tight_layout()

    anim = fa(fig, init_func=init, func=rotation, frames=np.concatenate([np.linspace(p*np.pi, (p+1)*np.pi, mt.ceil(np.pi*(2+1/(1+np.exp(p))))) for p in range(-20, 100)], axis=0),
            interval=0, blit=False) # change the volcety of point by adding 1, p to p+1 where p is mapping of custumized simoid function
    #anim.save('video.mp4', fps=60, writer='ffmpeg', dpi=300, bitrate=10**3)
    plt.show()
