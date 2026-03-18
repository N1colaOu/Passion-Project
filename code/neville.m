clear; clc; close all;

%--------------------
%Editable input data
x = [1, 2, 3];
y = [1, 4, 9];
x0 = 2.500;
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
        p(i,j) = ((x0-x(i)) * p(i+1,j-1) - (x0-x(i+j-1)) * p(i,j-1)) / (x(i+j-1)-x(i));
    end
end
disp(p);
%disp(p(1,n));