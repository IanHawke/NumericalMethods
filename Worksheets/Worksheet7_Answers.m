%
% Suggested model answers to worksheet 7
%
% Ian Hawke, 16/4/08
%

% Clear all starting values.
clear;
close all;
clc;

% Coding question 1; elliptic equations

disp('Question 1')

% Once again the following should be written as a function.

% Set up the domain
interval = [0 1 0 1];
% Set up the function
f = @(x,y)(sin(pi*y).*(2-6*x-(pi*x).^2.*(1-x)));

Nconvergence = 8;
errs = zeros(Nconvergence, 1);
ind = zeros(size(errs));
for n = 1:Nconvergence
    Nx = 2 + 8*n; Ny = 2 + 8*n;
    ind(n) = Nx;
    hx = (interval(2)-interval(1))/(Nx+1);
    hy = (interval(4)-interval(3))/(Ny+1);
    alpha = (hx/hy)^2;

    x = linspace(interval(1),interval(2),Nx+2);
    y = linspace(interval(3),interval(4),Ny+2);
    [X,Y]=ndgrid(x,y);

    % Set up the boundary conditions.
    U = zeros(Nx+2,Ny+2);
    U(1   ,:   ) = 0;
    U(Nx+2,:   ) = 0;
    U(:   ,1   ) = 0;
    U(:   ,Ny+2) = 0;

    A = diag(-2*(1+alpha)*ones(Nx*Ny,1));
    b = zeros(Nx*Ny,1);
    % Natural ordering by columns
    for j = 1:Ny
        for i = 1:Nx
            % The row index given by natural ordering by columns.
            k = j + Ny*(i-1);
            % The right hand side vector
            b(k) = hx^2*f(x(i+1),y(j+1));
            if (i == 1)
                b(k) = b(k) - 0;
            elseif (i == Nx)
                b(k) = b(k) - 0;
            end
            if (j == 1)
                b(k) = b(k) - 0;
            elseif (j == Ny)
                b(k) = b(k) - 0;
            end
            % The laplacian stencil
            if (j > 1)
                A(k, k-1) = alpha;
            end
            if (j < Ny)
                A(k, k+1) = alpha;
            end
            if (i > 1)
                A(j+Ny*(i-2),k) = 1;
            end
            if (i < Nx)
                A(j+Ny*(i  ),k) = 1;
            end
        end
    end
    % Solve the interior
    Uint = A\b;
    for j = 1:Ny
        for i = 1:Nx
            k = j + Ny*(i-1);
            U(i+1,j+1) = Uint(k);
        end
    end
    Uexact = X.^2.*(1-X).*sin(pi*Y);
    errs(n) = sqrt(sum(sum((U-Uexact).^2))/Nx/Ny);
end
figure
loglog(1./ind,errs,'kx',1./ind,0.05./ind.^2,'b-')
xlabel('h');ylabel('|Error|');
legend('Finite difference','\propto h^2','Location','NorthWest')
title('Second order convergence for the Poisson equation')


% Coding question 2; FTBS for the advection equation, periodic boundaries

disp('Question 2')

interval = [0 1];
% We define the time step from c, instead of the other way around.
c = 0.5;
errorFTBS = zeros(5,1);
npFTBS=zeros(size(errorFTBS));
for nconv = 1:7
    npoints = 60*2^(nconv-1)-1;
    h = (interval(2) - interval(1)) / (npoints + 1);
    delta = c * h;
    tend = 1;
    nt = round(tend/delta);

    x = linspace(interval(1),interval(2),npoints+2);
    % Initial data; a sine wave, period 2 pi
    y0 = sin(2 * pi * x);
    ynew = zeros(size(y0));
    yold = y0;

    t = 0;
    xexact = linspace(interval(1),interval(2),1001) - t;
    for i = 1:length(xexact)
        if (xexact(i) < 0)
            xexact(i) = xexact(i) + 1;
        end
    end

    for n = 1:nt
        for i = 2:npoints+2
            % This is the actual FTBS algorithm
            ynew(i) = yold(i) - c * (yold(i) - yold(i-1));
        end
        %Boundary conditions; periodic
        ynew(1) = yold(npoints+2);
        t = t + delta;
        yold = ynew;
    end
    hold off;

    % As the final time is after one period, and we are using periodic
    % boundaries, the correct answer is the initial data!
    errorFTBS(nconv) = norm(ynew - y0)/sqrt(npoints);
    npFTBS(nconv) = npoints;
end
figure
loglog(1./npFTBS,errorFTBS,'kx',1./npFTBS,1./npFTBS)
xlabel('h')
ylabel('|Error|')
title('Convergence of FTBS for advection equation')
legend('Numerical Error','\propto h');


% Coding question 3; traffic flow equation

disp('Question 3')

interval = [-10 10];
% We define the time step from c, instead of the other way around.
c = 0.5;

npoints = 200 - 1;
h = (interval(2) - interval(1)) / (npoints + 1);
delta = c * h;
tend = 0.5;
nt = round(tend/delta);

x = linspace(interval(1),interval(2),npoints+2);
% Initial data 1; a gaussian
y0 = exp(-x.^2);
ynew = zeros(size(y0));
yold = y0;

t = 0;

for n = 1:nt
    for i = 2:npoints+2
        % This is the actual FTBS algorithm applied to the traffic equation
        ynew(i) = yold(i) - c * (yold(i) * (1 - yold(i)) - yold(i-1) * (1 - yold(i-1)));
    end
    %Boundary conditions; static, just to put something down.
    ynew(1) = yold(1);
    t = t + delta;
    yold = ynew;
end
figure
subplot(1,3,1)
plot(x,ynew,'bo-')
xlabel('x');ylabel('y');
title('Traffic flow, initial gaussian')


% Initial data 2; a discontinuous function
y0 = 0.2 + 1.2 * heaviside(x);
ynew = zeros(size(y0));
yold = y0;

t = 0;

for n = 1:nt
    for i = 2:npoints+2
        % This is the actual FTBS algorithm applied to the traffic equation
        ynew(i) = yold(i) - c * (yold(i) * (1 - yold(i)) - yold(i-1) * (1 - yold(i-1)));
    end
    %Boundary conditions; static, just to put something down.
    ynew(1) = yold(1);
    t = t + delta;
    yold = ynew;
end

subplot(1,3,2)
plot(x,ynew,'bo-')
xlabel('x');ylabel('y');
title('Traffic flow, initial discontinuous')


% Initial data 3; a different Heaviside
y0 = 1 - heaviside(x);
ynew = zeros(size(y0));
yold = y0;

t = 0;

for n = 1:nt
    for i = 2:npoints+2
        % This is the actual FTBS algorithm applied to the traffic equation
        ynew(i) = yold(i) - c * (yold(i) * (1 - yold(i)) - yold(i-1) * (1 - yold(i-1)));
    end
    %Boundary conditions; static, just to put something down.
    ynew(1) = yold(1);
    t = t + delta;
    yold = ynew;
end
subplot(1,3,3)
plot(x,ynew,'bo-')
xlabel('x');ylabel('y');
title('Traffic flow, initial discontinuous again')

disp('At the discontinuity the algorithm fails, whether in the initial data or forming later')
disp('Looking at the gaussian case we see that the discontinuity forms at x < 0')
disp('This suggests that the shock is moving backwards, and that the associated characteristics have negative speed')
disp('Hence FTFS may work better (try it!)')

