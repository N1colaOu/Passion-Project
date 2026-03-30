import numpy as np
import matplotlib.pyplot as plt

#PDE being solved :  du^2/dx^2 * const = du/dt , where u is temp
#the information given : const, u(all x, 1)

##----------Start of editable input data
N = 100  # # steps                            
x_max = 100 #cm                     
t_max = 30 #s                        
T0 = np.random.randint(1, 5, N) #inital distribution
T0[0] = 2   #boundary condition
T0[-1] = 2   #boundary condition
coeff = 1   #physical coefficient (0 1(+-1)]                                                 
##-----------End of editable input data

#function that calculates the second derivative at points x and t
def uxx(u, x, t):
    return u[x+1, t] - 2*u[x, t] + u[x-1, t]

#function that calculates the next temperature value
def u_next(u, x, t0, u_t):
    return u[x, t0] + u_t[x, t0]


n_t = N#*2
n_x = len(T0)
u = np.zeros((n_x, n_t))
u[:, 0] = T0
dt = t_max/n_t #step size in t
dx = x_max/n_x #step size in x
du_dxx = np.zeros_like(u)
du_dxx[:, 0] = T0
du_dt = np.zeros_like(u)
du_dt[:, 0] = T0

coeff = dt*coeff/dx**2

#f = figure
#f.Visible = 'off'
#M(n_t) = struct('cdata', [], 'colormap', [])
for j in range(n_t-1):
    for i in range(1,n_x-1):
        du_dxx[i, j] = uxx(u, i, j) #get temp_xx value for all points on x
    du_dt[:, j] = du_dxx[:, j]*coeff #get temp_t value for all points on x
    #plot(u(:, j))
    #M(j) = getframe
    for i in range(n_x):
        u[i, j+1] = u_next(u, i, j, du_dt) #get temp value for all points on x after dt has passed
#plot(u(:, n_t))
#M(n_t) = getframe
#f.Visible = 'on'
#movie(M)


#Remove comment to plot the surface 
t = np.linspace(0, t_max, n_t) 
x = np.linspace(0, x_max, n_x)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(t, x, u, edgecolor='none', cmap='viridis')
ax.set_title('One Dimensional Numerical Heat Equation')
ax.set_ylabel('Position on rod')
ax.set_xlabel('Position in time')
ax.set_zlabel('Heat')
plt.show()
