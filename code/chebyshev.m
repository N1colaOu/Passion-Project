clear; clc; close all;

function res = cheb(n)
x = zeros(1, n);
for i = 0:n-1
    x(i+1) = cos((i+0.500)*pi/n);
end
res = x;
end
function res = f(x)
res = 1./(1+25*x.^2);
end
function res = newton_coeff(x, y)
n = length(x);
f_s = zeros(n, n);
f_s(:, 1) = y;
for i = 2:n
    for j = 1:n-i+1
        f_s(j, i) = (f_s(j+1, i-1) - f_s(j, i-1)) / (x(i+j-1) - x(j));
    end
end
res = f_s(1, :);
end
function res = newton(coeffs, x, x_data)
n = length(x_data);
res = zeros(1, length(x));
for i = 1:n
    base_pol = ones(1, length(x));
    for j = 1:i-1
        base_pol = base_pol.*(x-x_data(j));
    end
    res = res + base_pol*coeffs(i);
end

end
n = 20;

x_cheb = cheb(n);
y_cheb = f(x_cheb);

x_equi = linspace(-1, 1, n);
y_equi = f(x_equi);

t = linspace(-1, 1, 100);
coeffs_cheb = newton_coeff(x_cheb, y_cheb);
to_plot_cheb = newton(coeffs_cheb, t, x_cheb);

coeffs_equi = newton_coeff(x_equi, y_equi);
to_plot_equi = newton(coeffs_equi, t, x_equi);

hold on;
plot(t, to_plot_equi, Color='r');
plot(t, to_plot_cheb, Color='b');
plot(t, f(t), Color='g');
legend("Equidistnand Nodes", "Chebyshev Nodes", "Runge's Function", fontsize=15);
