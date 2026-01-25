N = 300;

% Spatial domain (normalized rod length)
x = linspace(0, 1, N);

% Gaussian parameters
mu = 0.5;        % center of the rod
sigma = 0.1;     % width of the Gaussian
A = 100;           % peak temperature amplitude

% Gaussian temperature distribution
%T0 = A * exp(-((x - mu).^2) / (2 * sigma^2));
T0 = sin(pi * x *2);
%T0 = 
T0(1) = 0;
T0(end) = 0;
plot(T0);
% Save to .mat file
save('temperature_initial.mat', 'T0');