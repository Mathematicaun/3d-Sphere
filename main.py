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
_ = np.linspace(0, w, 30)
stepsL = stepsS = .4
t1, t2 = np.meshgrid(_, _)
if r + Z >= n or -r + Z <= -n:
    print('the sphere is out of the space')
else:
    ax.plot_surface(r*np.cos(t1)*np.cos(t2), r*np.cos(t1)*np.sin(t2), r*np.sin(t1), color='none', edgecolor='white', alpha=.4)

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
