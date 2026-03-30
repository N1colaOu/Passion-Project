import numpy as np
import matplotlib.pyplot as plt
#------------------------------------
# y' = f(t, y) for first order ode of the type
# y should be continous and smooth for all t !!!!!
def f(t, y):
#input your function here
    return y - 0.5*np.exp(t/2)*np.sin(5*t) + 5*np.exp(t/2)*np.cos(5*t)
h = 0.05
t_start = 0.0
t_end = 10.0
y0 = 0.0
#------------------------------------%


def y_n1(t_n, y_n, h):
    A_coeff = f(t_n, y_n)
    B_coeff = f(t_n + h/2, y_n + A_coeff * h / 2)
    C_coeff = f(t_n + h/2, y_n+ B_coeff * h / 2)
    D_coeff = f(t_n + h, y_n + C_coeff * h)
    return y_n + (A_coeff + 2*B_coeff +  2*C_coeff + D_coeff)* h / 6


t_span = float(np.abs(t_end - t_start))
n = int(t_span/h)
t = np.linspace(t_start, t_end, n)
y = np.zeros(n, dtype=float)
y[0] = y0
for i in range(0, n-1):
    y[i+1] = y_n1(t[i], y[i], h)


fig1, ax1 = plt.subplots(figsize = (6, 5), layout = 'constrained')
ax1.plot(t, y)

ax1.set_xlabel('t')
ax1.set_ylabel('y(t)')
ax1.legend(['RK4'])
ax1.set_title('RK4')
plt.show()