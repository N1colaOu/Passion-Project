import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

min_x_val = 0.6
max_x_val = 1
min_y_val = 0
max_y_val = 0.4
num_pts = 300
conv_rad = 2
iter = 50
const = -0.75 + 0.4j

def get_divergence_rate(mesh, iterations, radius, f):    
    z = mesh.copy()
    div_rate = np.zeros(mesh.shape)
    for i in range(iterations):
        bool_idx = np.abs(z) < radius
        z[bool_idx] = f(z[bool_idx])
        div_rate[bool_idx] += 1
    return div_rate

def plot_fractal(mnxv, mxxxv, mnyv, mxyv, f, numpts = 300, convrad = 2, iter = 50):
    x, y = np.meshgrid(np.linspace(mnxv, mxxxv, numpts), np.linspace(mnyv, mxyv, numpts))
    mesh = x +y*1j
    to_plot = get_divergence_rate(mesh, iter, convrad, f)
    fig, ax = plt.subplots(figsize=(12.5, 10))
    ax.scatter(x, y, c=to_plot)
    fig.colorbar(mpl.cm.ScalarMappable(norm=mpl.colors.Normalize(0, iter), cmap="plasma"), ax = ax, label = "Iterations to diverge")
    ax.set_xlabel('Real axis')
    ax.set_ylabel('Imaginary axis')
    plt.show()

def plot_set1():
    def f(z):
        return np.square(z) -0.75 + 0.4j
    plot_fractal(-1, 1, -1, 1, f)
def plot_set2():
    def f(z):
        return np.square(z) + np.pi/10
    plot_fractal(-1, 1, -1, 1, f)
def plot_set3():
    def f(z):
        return np.square(z) + np.pi/11.2
    plot_fractal(0, 1, 0.155, 1.155, f)
def plot_set4():
    def f(z):
        return np.square(z) -0.79 + 0.15j
    plot_fractal(-1.5, 1.5, -1.5, 1.5, f)
def plot_set5():
    def f(z):
        return np.square(z) - 1.476
    plot_fractal(-1.5, 1.5, -1.5, 1.5, f)
def plot_set6():
    def f(z):
        return np.square(z) - 0.12 - 0.77j
    plot_fractal(-1.5, 1.5, -1.5, 1.5, f)

plot_set3()