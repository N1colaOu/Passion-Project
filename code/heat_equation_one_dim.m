clear; clc; close all;

%PDE being solved :  du^2/dx^2 * const = du/dt , where u is temp
%the information given : const, u(all x, 1)

%%----------Start of editable input data
N = 100;  % # steps                            
x_max = 100; %cm                     
t_max = 30; %s                        
T0 = randi(4, 1, N); %inital distribution
T0(1) = 2;   %boundary condition
T0(N) = 2;   %boundary condition
coeff = 1;   %physical coefficient (0; 1(+-1)]                                                 
%%-----------End of editable input data


%function that calculates the second derivative at points x and t
function res = uxx(u, x, t) 
    res = (u(x+1, t) - 2*u(x, t) + u(x-1, t));
end
%function that calculates the next temperature value
function res = u_next(u, x, t0, u_t)
    res = u(x, t0) + u_t(x, t0);
end

n_t = N*2;
n_x = length(T0);
u = zeros(n_x, n_t);
u(:, 1) = T0;
dt = t_max/n_t; %step size in t
dx = x_max/n_x; %step size in x
du_dxx = u;
du_dt = u;

coeff = dt*coeff/dx^2;

%f = figure;
%f.Visible = 'off';
%M(n_t) = struct('cdata', [], 'colormap', []);
for j = 1:n_t-1
    for i = 2:n_x-1
        du_dxx(i, j) = uxx(u, i, j); %get temp_xx value for all points on x
    end
    du_dt(:, j) = du_dxx(:, j)*coeff; %get temp_t value for all points on x
    %plot(u(:, j));
    %M(j) = getframe;
    for i = 1:n_x
        u(i, j+1) = u_next(u, i, j, du_dt); %get temp value for all points on x after dt has passed
    end
    
end
%plot(u(:, n_t));
%M(n_t) = getframe;
%f.Visible = 'on';
%movie(M);


%Remove comment to plot the surface 
t = linspace(0, t_max, n_t); 
x = linspace(0, x_max, n_x);
s = surf(t, x, u, 'EdgeColor', 'none', 'FaceColor', 'interp');
title('One Dimensional Numerical Heat Equation', 'FontSize', 20, 'FontWeight', 'bold');
ylabel('Position on rod', 'FontSize', 15, 'FontWeight', 'bold');
xlabel('Position in time', 'FontSize', 15, 'FontWeight', 'bold');
zlabel('Heat', 'FontSize', 15, 'FontWeight', 'bold');
