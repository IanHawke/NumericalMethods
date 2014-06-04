%
% Suggested model answers to worksheet 6
%
% Ian Hawke, 15/4/08
%

% Clear all starting values.
clear;
close all;
clc;

% Coding question 1; shooting method.
%
% The first order system will be:
%
% v(1)' = (y)'  = y'         =   v(2)
% v(2)' = (y')' = 3 y' - 2 y = 3 v(2) - 2 v(1)
%

disp('Question 1')

% The RHS function for the system.
dvdx = @(x,v)([v(2); 3*v(2) - 2*v(1)]);

% Bracket the guess for the bisection search
z_lo = -10;
z_hi =  10;
phi_lo = Worksheet6_MyShootingPhi(dvdx, z_lo);
phi_hi = Worksheet6_MyShootingPhi(dvdx, z_hi);
if (phi_lo * phi_hi > 0)
    error('Failed to bracket initial root?')
end

% Bisection search
tolerance = 1e-14;
z = (z_lo + z_hi) / 2;
phi = Worksheet6_MyShootingPhi(dvdx, z);
while (z_hi - z_lo > tolerance)
    if (phi * phi_lo < 0)
        z_hi   = z;
        phi_hi = phi;
    else
        z_lo   = z;
        phi_lo = phi;
    end
    z = (z_lo + z_hi) / 2;
    phi = Worksheet6_MyShootingPhi(dvdx, z);
end
% Having found sufficiently good initial data, get the "true" solution
sol = ode45(dvdx, [0 1], [0;z]);
x  = linspace(0,1,101);
xf = linspace(0,1,1001);
yexact = (exp(2*xf-1)-exp(xf-1))./(exp(1)-1);
y = deval(sol, x, 1);
errs = yexact - deval(sol, xf, 1);
subplot(1,2,1)
plot(x, y, 'kx', xf, yexact, 'b-')
xlabel('x');ylabel('y');legend('Shooting method', 'Exact')
subplot(1,2,2)
plot(xf, errs)
xlabel('x');ylabel('Error')

% Question 2; finite difference BVPs

disp('Question 2')

% We want to set up the linear system for y'' - 3 y' + 2 y = 0, y(0) = 0,
% y(1) = 1.
%
% Central differencing gives
%
% y_{i-1} (1 + 3 h / 2) - y_{i} (2 - 2 h^2) + y_{i+1} (1 - 3 h / 2) = 0
%
% in the interior, with y_0 = 0 and y_{N+1} = 1.
%
% For simplicity of presentation we set this up using a loop over matrix
% rows.

Nconvergence = 12;
errs = zeros(Nconvergence, 1);
ind = zeros(size(errs));
for n = 1:Nconvergence
   
    Np = 1 + 2^(n);
    ind(n) = Np;
    h = 1 / (Np + 1);
    
    A = zeros(Np);
    b = zeros(Np, 1);
    
    % Set the interior matrix entries
    for i = 2:Np-1
        A(i, i-1) = 1 + 3 * (h / 2);
        A(i, i  ) = -2 + 2 * h^2;
        A(i, i+1) = 1 - 3 * (h / 2);

        b(i) = 0;
    end
    
    % Set the boundary entries.
    
    A(1, 1) = -2 + 2 * h^2;
    A(1, 2) = 1 - 3 * (h / 2);
    A(Np, Np  ) = -2 + 2 * h^2;
    A(Np, Np-1) = 1 + 3 * (h / 2);

    b(1)  = 0;
    b(Np) = 3 * (h / 2) - 1;

    % Solve the linear system
    
    y = zeros(Np + 2, 1);
    y(1) = 0; y(Np + 2) = 1;
    y(2:Np+1) = A \ b;
    
    x = linspace(0, 1, Np + 2);
    ye = (exp(2*x-1)-exp(x-1))./(exp(1)-1);
    errs(n) = norm(y - ye')/norm(ye);
    
end
figure
loglog(1./(ind + 1), errs, 'kx', 1./(ind + 2), 0.5./(ind + 1).^2)
xlabel('x');ylabel('|Error|')
legend('Finite difference','\propto h^2','Location','NorthWest')

% Question 3; finite difference BVPs, Neumann BCs

disp('Question 3')

% The same as above, just modifying the right boundary.

Nconvergence = 12;
errs = zeros(Nconvergence, 1);
ind = zeros(size(errs));
for n = 1:Nconvergence
   
    Np = 1 + 2^(n);
    ind(n) = Np;
    h = 1 / (Np + 1);
    
    A = zeros(Np);
    b = zeros(Np, 1);
    
    % Set the interior matrix entries
    for i = 2:Np-1
        A(i, i-1) = 1 + 3 * (h / 2);
        A(i, i  ) = -2 + 2 * h^2;
        A(i, i+1) = 1 - 3 * (h / 2);

        b(i) = 0;
    end
    
    % Set the boundary entries.
    
    A(1, 1) = -2 + 2 * h^2;
    A(1, 2) = 1 - 3 * (h / 2);
    % The next line is modified for Neumann BCs
    A(Np, Np  ) = -2 + 2 * h^2 + 1 - 3 * (h / 2);
    A(Np, Np-1) = 1 + 3 * (h / 2);

    b(1)  = 0;
    % The next line is modified for Neumann BCs
    b(Np) = -h * (1 + exp(1) / (exp(1) - 1)) * (1 - 3 * (h / 2));

    % Solve the linear system
    
    y = zeros(Np + 2, 1);
    y(1) = 0; y(Np + 2) = 1;
    y(2:Np+1) = A \ b;
    
    x = linspace(0, 1, Np + 2);
    ye = (exp(2*x-1)-exp(x-1))./(exp(1)-1);
    errs(n) = norm(y - ye')/norm(ye);
    
end
figure
loglog(1./(ind + 1), errs, 'kx', 1./(ind + 2), 1./(ind + 1).^1)
xlabel('x');ylabel('|Error|')
legend('Finite difference, Neumann','\propto h','Location','NorthWest')
