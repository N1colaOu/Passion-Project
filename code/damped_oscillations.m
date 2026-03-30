clear; clc; close all;

% x'' + 2px' +w^2x = 0
%---------------------------------%
N = 500; % accuracy
x0 = 1; % m
v0 = 3; % m/s
t_min = 0; % s
t_max = 10; % s
p = 0.5; % 
w = 5; % 
%---------------------------------%

step_size = (t_max-t_min)/N;
t = linspace(t_min, t_max, N);
if  p < w % complex case, aka under-damped
    gamma = sqrt(w^2-p^2);
    c1 = x0;
    c2 = (v0+p*x0)/gamma;
    A = sqrt(c1^2 + c2^2);
    Phi = -atan(c2/c1);
    x = exp(-p*t)*A.*cos(gamma*t+Phi);
    name = 'Under-Damped Oscilations';
elseif p > w % real case with diff roots over-damped
    a = -p;
    b = sqrt(p^2-w^2);
    B = (a*x0+b*x0-v0)/(2*b);
    A = (b*x0-a*x0+v0)/(2*b);
    x = A*exp((a+b)*t) + B*exp((a-b)*t);
    name = 'Over-Damped Oscilations';
else % p = w critically damped
    A = x0;
    B = v0+p*A;
    x = A*exp(-p*t) + B.*t.*exp(-p*t);
    name = 'Critically-Damped Oscilations';
end
plot(t, x, 'LineWidth', 3.4);
xlabel('time [s]', 'FontSize', 20);
ylabel('position in time [m]', 'FontSize', 20);
title(name, 'FontSize', 20);
legend('x(t)', fontsize = 30);
