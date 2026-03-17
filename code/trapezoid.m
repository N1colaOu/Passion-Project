clear; clc; close all;

%-----------------------
%Editable parameters:
numPoints = 25;
x_start = 0;
x_end = 10;
func = @(x) cos(x);
%-----------------------


x = linspace(x_start, x_end, numPoints);
area = 0;
for i = 1:numPoints-1
    area = area + (func(x(i)) + func(x(i+1)))/2*(x(i+1) - x(i));
end
%disp(area);

plot(x, func(x), 'Color',"r");
hold on;
pretty_x = linspace(x_start, x_end, 10000);
plot(pretty_x, func(pretty_x), 'Color', "b");
xlabel("x", "FontSize", 20);
ylabel("f(x)", "FontSize", 20);
title("Trapezoid Integration", "FontSize", 20);
legend("Approximation", "Real Function", 'Fontsize', 20);
hold off;

disp(['Calculated area under the curve: ', num2str(area)]);
