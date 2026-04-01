import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#PDE being solved :  du^2/dx^2 * const = du/dt , where u is temp
#the information given : const, u(all x, 0)

##----------Start of editable input data
N = 100  # # steps                            
x_max = 100 #cm                     
t_max = 30 #s

u_max = 2 #max_temp for random gen
u_min = -2 #miNemp for random gen

u_start = 0   #boundary condition
u_end = 0   #boundary condition

coeff = 0.2   #physical coefficient (0 1(+-1)]                                                 
##-----------End of editable input data

#function that calculates the second derivative at points x and t
def uxx(u, x, t):
    return u[x+1, t] - 2*u[x, t] + u[x-1, t]


T0 = np.random.randint(u_min, u_max, N)
u = np.zeros((N, N))
T0[0] = u_start
T0[-1] = u_end
u[:, 0] = T0[:]
dt = t_max/N #step size in t
dx = x_max/N #step size in x
#du_dxx = np.zeros_like(u)
du_dxx = np.copy(u)
#du_dt = np.zeros_like(u)
du_dt = np.copy(u)

coeff = dt*coeff/(dx**2)
for j in range(N-1):
    for i in range(1,N-1):
        du_dxx[i, j] = uxx(u, i, j) #get curr_xx value for all points on x
    du_dt[:, j] = du_dxx[:, j]*coeff #get curr_t value for all points on x
    for i in range(N):
        u[i, j+1] = u[i, j] + du_dt[i, j] #get temp value for all points on x after dt has passed

t = np.linspace(0, t_max, N) 
x = np.linspace(0, x_max, N)

x, t = np.meshgrid(x, t)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize = (10, 9))
ax.plot_surface(x, t, u, edgecolor='none', cmap='viridis')
ax.set(xlim=[0, x_max], ylim = [0, t_max] , zlim=[u_min, u_max], ylabel='Positon [m]', xlabel='Time [s]', zlabel = "Temp [C]", title = "One Dimensional Numerical Heat Equation")
plt.show()
"""
fig, ax = plt.subplots(figsize = (10, 9))
line, = ax.plot([], [], lw = 2) 
ax.set(xlim=[0, x_max], ylim=[u_min, u_max-1], xlabel='Positon [m]', ylabel='Temperature [C]', title = "One Dimensional Numerical Heat Equation")
ydata = np.zeros((1, N))
def update(frame):
    ydata = u[:, frame]
    line.set_data(x, ydata)
    return line,
ani = animation.FuncAnimation(fig=fig, func=update, frames=N, interval=30)
plt.show()
"""
#ani.save("heat_1d.gif")


