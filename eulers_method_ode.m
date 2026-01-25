clear; clc; close all;

function res = y_n1(y_n, t_n, t_n1)
    res = y_n + f(t_n, y_n)*(t_n1 - t_n);
end
%%%%%%%%%%%%%%%%%%%%%%%%%%% Changes for the data are made here
function res = f(t, y) % y' = f(t, y) for ode of the type
    res = y - 0.5*exp(t/2)*sin(5*t) + 5*exp(t/2)*cos(5*t);
end
function res = y_anal(t)
    res = exp(t/2).*sin(5*t);
end
n = 100000;
t_end = 10;
t_start = 0;

t_data = linspace(0, t_end, n);
y_data = zeros(1, n);
y_data(1) = 0; %IVC
%%%%%%%%%%%%%%%%%%%%%%%%%%%
for i = 2:length(t_data)
    y_data(i) = y_n1(y_data(i-1), t_data(i-1), t_data(i));
end
y_real = y_anal(t_data);

difference_sqrd = 1 - sum((y_real-y_data).^2)/sum((y_real-mean(y_real)).^2);
disp(difference_sqrd);% if its 1 -> "perfect  fit"
figure;
hold on;
grid on;
plot(t_data, y_data, 'r-', 'LineWidth', 1, 'DisplayName','Euler');
plot(t_data, y_real, 'b-', 'LineWidth', 1, 'DisplayName', 'Analytic');
xlabel("t", "FontSize", 18);
ylabel("y", "FontSize", 18);
legend("Location", "best", "FontSize", 18);
title('Comparison of Numerical and Analytic Solutions', 'FontSize', 18);
