import numpy as np
import matplotlib.pyplot as plt

#------------------------------------%
# y' = f(t, y) for first order ode of the type
# y should be continous and smooth for all t !!!!   
def f(t, y):
#input your function here
    return y - 0.5*np.exp(t/2)*np.sin(5*t) + 5*np.exp(t/2)*np.cos(5*t)

h = 0.05
t_start = 0
t_end = 10
y0 = 0
#------------------------------------%
def A(t_n, y_n):
    return f(t_n, y_n)

def B(t_n, y_n, h):
   A_coeff = A(t_n, y_n)
   y_n1_temp = y_n + A_coeff*h
   t_n1 = t_n + h
   return f(t_n1, y_n1_temp)

def y_n1(t_n, y_n, h):
    A_coeff = A(t_n, y_n)
    B_coeff = B(t_n, y_n, h)
    return y_n + (A_coeff + B_coeff) * h / 2

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
ax1.legend(['RK2'])
ax1.set_title('RK2')

#plt.plot(t, y)

#plt.xlabel('t')
#plt.ylabel('y(t)')
#plt.legend(['RK2'])
#plt.title('RK2')


