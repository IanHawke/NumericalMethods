%
% Suggested model answers to worksheet 4
%
% Ian Hawke, 14/4/08
%

% Clear all starting values.
clear;
close all;
clc;

% Coding question 1; Euler's method

disp('Question 1')

f = @(x,y)(2 - exp(-4.*x)-2*y);
y0 = 1;
Nconvergence = 10;
y = zeros(Nconvergence, 1);
errs = zeros(size(y));
Npoints = zeros(size(y));
for i=1:Nconvergence
    Nsteps = 10*2^(i-1);
    Npoints(i) = Nsteps;
    y(i) = Worksheet4_MyEuler(f, y0, [0 1], Nsteps);
    errs(i) = abs(y(i) - 1 + (exp(-2) - exp(-4))/2);
end
loglog(1./Npoints, errs, 'kx', 1./Npoints, 0.1./Npoints,'b-')
legend('Euler', '\propto h','Location','SouthEast')
xlabel('h');ylabel('|Error|')
title('Convergence for Euler')
    
% Coding question 2; RK4

disp('Question 2')

for i=1:Nconvergence
    Nsteps = 10*2^(i-1);
    Npoints(i) = Nsteps;
    y(i) = Worksheet4_MyRK4(f, y0, [0 1], Nsteps);
    errs(i) = abs(y(i) - 1 + (exp(-2) - exp(-4))/2);
end
figure
loglog(1./Npoints, errs, 'kx', 1./Npoints, 0.01./(Npoints.^4),'b-')
legend('RK4', '\propto h^4','Location','SouthEast')
xlabel('h');ylabel('|Error|')
title('Convergence for RK4')

% Coding question 3; power method.

disp('Question 3')

% Make a random 3x3 matrix and check its eigenvalues
A=rand(3);
lambda_exact = eigs(A);

% Compute the eigenvalues to a given tolerance
tol = 1e-8;
niterations_max = 100;

% Should really check that A is square.
n=size(A,1);
%Initial guess is nearly all 1.
x0=ones(n,1)+1e-7*rand(n,1);
xn=zeros(n,niterations_max);
xn(:,1)=x0;
rn=zeros(n,1);
rn(1)=1;
for k = 2 : niterations_max
    xn(:,k-1) = xn(:,k-1)./norm(xn(:,k-1));
    xn(:,k) = A * xn(:, k-1);
    rn(k) = sum(xn(:,k))./sum(xn(:,k-1));
    if (abs(rn(k) - rn(k-1)) < tol)
        break
    end
end
lambda = rn(k);
disp(sprintf('Maximum eigenvalue from power method is %g; exact is %g (error %g)', ...
    lambda, lambda_exact(1), abs(lambda - lambda_exact(1))));

% Inverse power method.
% Initial guess is nearly all 1.
x0=ones(n,1)+1e-7*rand(n,1);
xn=zeros(n,niterations_max);
xn(:,1)=x0;
rn=zeros(n,1);
rn(1)=1;
for k = 2 : niterations_max
    xn(:,k-1) = xn(:,k-1)./norm(xn(:,k-1));
    xn(:,k) = A \ xn(:, k-1);
    rn(k) = sum(xn(:,k))./sum(xn(:,k-1));
    if (abs(rn(k) - rn(k-1)) < tol)
        break
    end
end
niterations = k;
lambda = 1./rn(k);
disp(sprintf('Minimum eigenvalue from power method is %g; exact is %g (error %g)', ...
    lambda, lambda_exact(3), abs(lambda - lambda_exact(3))));

% Now check how the number of iterations varies with the size of the
% matrix.

MatrixSize = 20;
niters = zeros(MatrixSize-2,1);
errs = zeros(size(niters));
ind = zeros(size(niters));
for n = 3:MatrixSize
   
    A = rand(n);
    lambda_exact = eigs(A);
    %Initial guess is nearly all 1.
    x0=ones(n,1)+1e-7*rand(n,1);
    xn=zeros(n,niterations_max);
    xn(:,1)=x0;
    rn=zeros(n,1);
    rn(1)=1;
    for k = 2 : niterations_max
        xn(:,k-1) = xn(:,k-1)./norm(xn(:,k-1));
        xn(:,k) = A * xn(:, k-1);
        rn(k) = sum(xn(:,k))./sum(xn(:,k-1));
        if (abs(rn(k) - rn(k-1)) < tol)
            break
        end
    end
    niters(n-2) = k;
    lambda = rn(k);
    errs(n-2) = abs(lambda - lambda_exact(1));
    ind(n-2) = n;
    
end
figure
subplot(1,2,1)
plot(ind,niters,'kx')
xlabel('Matrix size');ylabel('N iterations');
subplot(1,2,2)
semilogy(ind,errs,'kx')
xlabel('Matrix size');ylabel('|Error|');
