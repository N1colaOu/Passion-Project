clear; clc; close all;
function res = y_n1(t_n, y_n, h)
    A_coeff = f(t_n, y_n);
    B_coeff = f(t_n + h/2, y_n + A_coeff * h / 2);
    C_coeff = f(t_n + h/2, y_n+ B_coeff * h / 2);
    D_coeff = f(t_n + h, y_n + C_coeff * h);
    res = y_n + (A_coeff + 2*B_coeff +  2*C_coeff + D_coeff)* h / 6;
end
%------------------------------------%
% y' = f(t, y) for first order ode of the type
% y should be continous and smooth for all t !!!!
function res = f(t, y)
%input your function here
    res = y - 0.5*exp(t/2)*sin(5*t) + 5*exp(t/2)*cos(5*t);
    %res = y - t.^2 + 1;
end
h = 0.05;
t_start = 0;
t_end = 10;
y0 = 0;
%------------------------------------%

t_span = abs(t_end - t_start);
n = t_span/h;
t = linspace(t_start, t_end, n);
y = zeros(1, n);
y(1) = y0;
for i = 1:n-1
    y(i+1) = y_n1(t(i), y(i), h);
end
hold on;
grid on;
plot(t, y, 'LineWidth', 1, 'LineStyle', '-', 'Color', 'r');

[t_matlab,y_matlab] = ode45(@(t, y) f(t, y), t, y(1));
plot(t_matlab, y_matlab, 'LineWidth', 1, 'LineStyle', '--', 'Color', 'b');


xlabel('t', 'FontSize', 20);
ylabel('y(t)', 'FontSize', 20);
lgd = legend('RK4', 'ODE45', 'Location', 'northwest');
title(lgd,'Numerical Comparison');
fontsize(lgd, 15, 'points');

fgr = figure;
error_arr = zeros(1, n);
for i = 1:n
    error_arr(i) = abs(y_matlab(i) - y(i));
end
figure(fgr);
plot(t, error_arr, 'LineWidth', 2, 'Color', 'g');
xlabel('t', 'FontSize', 20);
ylabel('Error (t)', 'FontSize', 20);
title('Error between RK4 and ODE45', 'FontSize', 20);
grid on;
lgd = legend('Difference', 'Location', 'northwest');
title(lgd,'Error Estimation');
fontsize(lgd, 15, 'points');