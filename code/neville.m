clear; clc; close all;

%--------------------
%Editable input data
x = [0.2000, 0.4000, 0.8000, 1.0000, 1.4000];
y = [0.1987, 0.3894, 0.7174, 0.8415, 0.9855];
x0 = 0.4500;
%--------------------

n = length(x);
%x_tosort = abs(x - x0);
%[x_tosort, I] = sort(x_tosort);
%x = x(I);
%y = y(I);
%check these

p = zeros(n, n);
for i = 1:n
    p(i, 1) = y(i);
end
for j = 2:n
    for i = 1:n-j+1
        p(i, j) = ((x0-x(i))*p(i+j-1, j-1) - (x0-x(i+j-1))*p(i, j-1))/(x(i+j-1)-x(i));
    end
end
disp(p);