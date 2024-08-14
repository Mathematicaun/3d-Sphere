import numpy as np
import matplotlib.pyplot as plt

# you can uncomment the following code to use GUI to show the fiugre
# import customtkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

n = 5

# you can uncomment the following code to use GUI to show the fiugre
# root = tk.CTk()
# root.title('3 Dimensional Sphere')
# frame = tk.CTkFrame(
#     master=root
# )
# frame.pack(fill=tk.BOTH, expand=True)

fig = plt.figure()
ax = fig.add_subplot(projection='3d', aspect='equal')
# setting
def settings():
    fig.set_facecolor('#131315')
    ax.set_xlabel('x', color='pink')
    ax.set_ylabel('y', color='pink')
    ax.set_zlabel('z', color='pink')
    ax.set_facecolor('#131315')
    ax.xaxis.pane.set(visible=False)
    ax.yaxis.pane.set(visible=False)
    ax.zaxis.pane.set(visible=False)

    ax.xaxis._axinfo['grid'].update(color='none')
    ax.yaxis._axinfo['grid'].update(color='none')
    ax.zaxis._axinfo['grid'].update(color='none')

    ax.xaxis.line.set(color='#ebfb73')
    ax.yaxis.line.set(color='#ebfb73')
    ax.zaxis.line.set(color='#ebfb73')

    ax.set(
        xlim=[-n, n],
        ylim=[-n, n],
        zlim=[-n, n],
        xticks=np.arange(-n, n, 1),
        yticks=np.arange(-n, n, 1),
        zticks=np.arange(-n, n, 1)
    )

    ax.tick_params(axis='x', color='#ebfb73')
    ax.tick_params(axis='y', color='#ebfb73')
    ax.tick_params(axis='z', color='#ebfb73')

    # ax.set_xticklabels([f'{_}' for _ in np.arange(-min, min)], color='#ebfb73', font='serif')
    # ax.set_yticklabels([f'{_}' for _ in np.arange(-min, min)], color='#ebfb73', font='serif')
    # ax.set_zticklabels([f'{_}' for _ in np.arange(-min, min)], color='#ebfb73', font='serif')
settings()


X, Y, Z = 0, 0, 0
r = 4
w = 2*np.pi
_ = np.linspace(0, w, 100)
stepsL = stepsS = .4

if r + Z >= n or -r + Z <= -n:
    print('the sphere is out of the space')
else:
    for i in np.arange(0, 2*r, stepsL):
        ax.plot(
            np.sqrt(r**2 - (i-(Z+r))**2)*np.cos(_)+X,
            np.sqrt(r**2 - (i-(Z+r))**2)*np.sin(_)+Y,
            np.array([i]*len(_))+Z-r,
            color='c'
        )
    for i in np.arange(0, 2*r, stepsL):
        ax.plot(
            np.sqrt(r**2 - (i-(Y+r))**2)*np.sin(_)+Y,
            np.array([i]*len(_))+Y-r,
            np.sqrt(r**2 - (i-(Y+r))**2)*np.cos(_)+Z,
            color='c'
        )    
    for i in np.arange(0, 2*r, stepsL):
        ax.plot(
            np.array([i]*len(_))+X-r,
            np.sqrt(r**2 - (i-(X+r))**2)*np.cos(_)+Y,
            np.sqrt(r**2 - (i-(X+r))**2)*np.sin(_)+Z,
            color='c'
        )
    for i in np.arange(0, w, stepsS):
        ax.plot(
            r*np.cos(i)*np.cos(_)+X,
            r*np.sin(i)*np.cos(_)+Y,
            r*np.sin(_)+Z,
            color='c'
        )

ax.view_init(elev=0)
plt.show()
# you can uncomment the following code to use GUI to show the fiugre
# canvas = FigureCanvasTkAgg(
#     fig,
#     master=frame
# )
# canvas.draw()
# canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# root.mainloop()
