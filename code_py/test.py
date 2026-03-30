import numpy as np
import matplotlib.pyplot as plt

# PDE being solved : du^2/dx^2 * const = du/dt , where u is temp
# the information given : const, u(all x, 1)

##----------Start of editable input data
N = 100                         # number of time steps
x_max = 100                     # cm
t_max = 30                      # s
T0 = np.random.randint(1, 5, N) # initial distribution (1 to 4)
T0[0] = 2                       # boundary condition
T0[-1] = 2                      # boundary condition
coeff = 1                       # physical coefficient (0, 1(+-1)]
##-----------End of editable input data

# function that calculates the second derivative at points x and t
def uxx(u, x, t):
    # note: u is 2D: rows = space, columns = time
    return u[x+1, t] - 2*u[x, t] + u[x-1, t]

# function that calculates the next temperature value
def u_next(u, x, t0, u_t):
    return u[x, t0] + u_t[x, t0]

n_t = N
n_x = len(T0)
u = np.zeros((n_x, n_t))
u[:, 0] = T0                     # initial condition: all space, first time step

dt = t_max / n_t
dx = x_max / n_x
coeff_factor = dt * coeff / dx**2   # factor for finite difference scheme

du_dxx = np.zeros_like(u)        # will store second spatial derivative
du_dt  = np.zeros_like(u)        # will store time derivative

for j in range(n_t - 1):
    # compute second spatial derivative for interior points at time j
    for i in range(1, n_x - 1):
        du_dxx[i, j] = uxx(u, i, j)
    # compute time derivative for all points at time j
    du_dt[:, j] = du_dxx[:, j] * coeff_factor
    # update temperature for next time step
    for i in range(n_x):
        u[i, j+1] = u_next(u, i, j, du_dt)

# Plot the surface
t = np.linspace(0, t_max, n_t)
x = np.linspace(0, x_max, n_x)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(t, x, u)
ax.set_title('One Dimensional Numerical Heat Equation')
ax.set_ylabel('Position on rod')
ax.set_xlabel('Time')
ax.set_zlabel('Temperature')
plt.show()