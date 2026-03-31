import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# x'' + 2px' +w^2x = 0
#---------------------------------#
N = 500 # accuracy
x0 = 1 # m
v0 = 3 # m/s
t_min = 0 # s
t_max = 10 # s
p = 0.3 # 
w = 4 # 
#---------------------------------#

step_size = (t_max-t_min)/N
t = np.linspace(t_min, t_max, N)
if  p < w: # complex case, aka under-damped
    gamma = np.sqrt(w**2-p**2)
    c1 = x0
    c2 = (v0+p*x0)/gamma
    A = np.sqrt(c1**2 + c2**2)
    Phi = -np.atan(c2/c1)
    x = np.exp(-p*t)*A*np.cos(gamma*t+Phi)
    name = 'Under-Damped Oscilations'
elif p > w: # real case with diff roots over-damped
    a = -p
    b = np.sqrt(p**2-w**2)
    B = (a*x0+b*x0-v0)/(2*b)
    A = (b*x0-a*x0+v0)/(2*b)
    x = A*np.exp((a+b)*t) + B*np.exp((a-b)*t)
    name = 'Over-Damped Oscilations'
else: # p = w critically damped
    A = x0
    B = v0+p*A
    x = A*np.exp(-p*t) + B*t*np.exp(-p*t)
    name = 'Critically-Damped Oscilations'

fig, ax = plt.subplots(figsize = (9, 7))
x_max = x[np.argmax(x)]
x_min = x[np.argmin(x)]
line, = ax.plot([], [], lw = 2) 
ax.set(xlim=[t_min, t_max], ylim=[x_min, x_max], xlabel='Time [s]', ylabel='Position [m]', title = name)
xdata, ydata = [], [] 
def update(frame):
    if frame == 0:
        xdata.clear()
        ydata.clear()
        line.set_data([], []) 
    xdata.append(t[frame])
    ydata.append(x[frame])
    line.set_data(xdata, ydata)
    return line,
ani = animation.FuncAnimation(fig=fig, func=update, frames=N, interval=30)
plt.show()
#ani.save("oscillation.gif", writer=animation.PillowWriter(fps=30))
