clear; clc; close all;
load('temperature_initial.mat');

function res = uxx(u, x, t)
    res = (u(x+1, t) - 2*u(x, t) + u(x-1, t))/1;
end
function res = u_next(u, x, t0, u_t)
    res = u(x, t0) + u_t(x, t0);
end
n_x = length(T0);
n_t = 15*n_x;
u = zeros(n_x, n_t);
u(:, 1) = T0;
t = linspace(1, n_x, n_x);
x = linspace(1, n_t, n_t);
du_dxx = zeros(n_x, n_t);
du_dt = zeros(n_x, n_t);
for j = 1:n_t-1
    for i = 2:n_x-1
        du_dxx(i, j) = uxx(u, i, j);
    end
    du_dt(:, j) = du_dxx(:, j)/2;
    for i = 1:n_x
        u(i, j+1) = u_next(u, i, j, du_dt);
    end
end
surf(u, 'EdgeColor', 'none');
